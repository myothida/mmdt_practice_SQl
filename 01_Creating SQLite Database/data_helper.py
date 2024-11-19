import pandas as pd

class MMDTApplicationProcessor:
    def __init__(self, app_file, participants_file, output_dir):
        """
        Initializes the class with file paths and output directory.
        """
        self.app_file = app_file
        self.participants_file = participants_file
        self.output_dir = output_dir

    def preprocess_application_data(self):
        """
        Reads application data, renames columns, and creates a public version of the data.
        """
        df = pd.read_csv(self.app_file)

        # Define and merge question names
        merge_questions = [
            'Time', 'Email-01', 'Email-02', 'Name', 'Selected', 'Reasons', 'BOD', 'City',
            'State_Region', 'Country', 'Date_Leave_Country', 'Gender', 'Current_Situation',
            'Type_of_Internet', 'Device_used', 'School_Name', 'Academic_career', 'Contact',
            'Pre_Knowledge_Data', 'Course_Wish_Join', 'Dedicate_Learning_Time',
            'Personal_Professional_Goals', 'Reason_Right_Person', 'Personal_Professional_Challenges',
            'Others', 'Agree_Survey', 'National_ID', 'Declaration'
        ]

        # Rename columns
        app_questions = pd.DataFrame(df.columns, columns=['question'])
        app_questions['Short_Col_Names'] = merge_questions
        app_questions.to_csv(f"{self.output_dir}/questions.csv", index=False)
        df.columns = merge_questions

        # Remove Personal Identification data
        df_main = df.drop(columns=[
            'Email-01', 'Email-02', 'Reasons', 'Agree_Survey',
            'National_ID', 'Contact', 'Declaration'
        ])
        df_main['BOD'] = df_main['BOD'].apply(lambda x: str(x).split('/')[2])
        return df_main
        
    def process_selected_students(self, df_main):
        """
        Processes selected students to assign unique IDs and prepares the selected list.
        """
        df_main['Name'] = df_main['Name'].str.strip()
        df_selected = df_main[df_main['Selected'] == 'Yes'].reset_index(drop=True)
        df_selected['ID'] = df_selected.index
        df_selected['ID'] = df_selected['ID'].apply(lambda x: 'mmdt2024.' + f"{x + 1:03}")
        return df_selected

    def handle_dropouts_and_generate_final_list(self, df_selected, df_main):
        """
        Handles dropouts by replacing participants and generates the final selected list.
        """
        df_current = pd.read_csv(self.participants_file)

        # Identify dropouts
        drop_out_stu_list = df_current[~df_current['In Place of'].isna()][
            ['PARTICIPANT ID', 'PERSONAL Name']
        ]
        drop_out_stu_list['PERSONAL Name'] = drop_out_stu_list['PERSONAL Name'].str.strip()

        # Extract the information of repalced participants
        df_replace = drop_out_stu_list.merge(
            df_main, how='left', left_on='PERSONAL Name', right_on='Name'
        )
        df_replace = df_replace.drop(columns='Name')
        df_replace = df_replace.rename(columns={
            'PARTICIPANT ID': 'ID', 'PERSONAL Name': 'Name'
        })

        # Update selected DataFrame
        df_replace.set_index('ID', inplace=True)
        df_selected.set_index('ID', inplace=True)
        df_selected.loc[df_replace.index] = df_replace
        df_selected.reset_index(inplace=True)
        df_selected = df_selected.drop(columns = ['Name'], axis = 1)
        # Save final selected list
        df_selected.to_csv(f"{self.output_dir}/mmdt_selected_batch01.csv", index=False)


