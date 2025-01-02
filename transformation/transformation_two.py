from base_class.dev_class import BaseDev
from test_data import data_two


class TransFormClass(BaseDev):
    def add_time_stamp_to_df(self, df):
        df_with_time_stamp = self.add_start_end_time_columns(df)
        return df_with_time_stamp

    def adding_column_city(self, df, columns_to_add_in_df):
        df_with_city_column = self.add_columns(df, columns_to_add_in_df)
        return df_with_city_column

    def dropping_column_city(self, df, columns_to_drop):
        df_without_city_column = self.drop_columns_from_df(df, columns_to_drop)
        return df_without_city_column

    def captilize_name_column_content(self, column, dataframe):
        df_with_name_column_capital = self.col_to_upper(column, dataframe)
        return df_with_name_column_capital

    def execute_transformations(self):
        # Passing all arguments from data file
        df = data_two.df
        columns_to_add = data_two.columns_to_add 
        columns_to_drop = data_two.columns_to_drop
        column_to_capitalize = data_two.column_to_capitalize
        expected_df = data_two.expected_df
        # Add timestamp to the DataFrame
        df_with_time_stamp = self.add_time_stamp_to_df(df)
        
        # Add city column to the DataFrame
        df_with_city_column = self.adding_column_city(df_with_time_stamp, columns_to_add)
        final_df = df_with_city_column
        # # Drop city column from the DataFrame
        # df_without_city_column = self.dropping_column_city(df_with_city_column, columns_to_drop)
        
        # # Capitalize name column content
        # final_df = self.captilize_name_column_content(column_to_capitalize, df_without_city_column)
        
        # compare expected and actual df
        status = self.compare_two_df(final_df, expected_df)
        
        return status


