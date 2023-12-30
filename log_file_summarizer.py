class Summarizer:
    """
    Log file parser. It retrieves all warning and error lines from a log file and displays them separately in the terminal.

    Attributes:
        file_name_to_summarize (str): The name of the file to resume.

    Methods:
        read_log() -> dict: Reads the log file and returns a dictionary containing the logs.
        visualize_summerize(): Visualizes the logs by printing them to the console.

     visualize_summerize() Output:
        Here is an example output from a log file in which there are no warnings but two errors are present:
            WARNING LOGS:
            [ No warnings found ]

            ERROR LOGS:
            2000-01-01 00:00 - ERROR: First error message
            2000-01-01 00:01 - ERROR: Second error message

    Notes:
        - For this version to work as expected, the log file must be in the root directory.
    """
    def __init__(self, file_name_to_summarize: str):
        self.file_name_to_summarize = file_name_to_summarize
        self.logs = {'WARNING': [], 'ERROR': []}

    def read_log(self) -> dict:
        try:
            with open(self.file_name_to_summarize, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if 'WARNING' in line:
                        self.logs['WARNING'].append(line)
                    elif 'ERROR' in line:
                        self.logs['ERROR'].append(line)
        except FileNotFoundError:
            print(f"ERROR OCCURRED: The file '{self.file_name_to_summarize}' was not found.")
            print('Ensure that the file exists in the root directory.')
            print('If the file is located at the root. Verify that the name provided is correct in the implementation code.')
            exit()
        return self.logs

    def visualize_summerize(self):
        log_types = ['WARNING', 'ERROR']
        print(f'{self.file_name_to_summarize} SUMMARY:')
        for log_type in log_types:
            print(f'\n{log_type} LOGS:')
            if not self.logs[log_type]:
                print(f'[ No {log_type.lower()}s found ]')
            else:
                for log in self.logs[log_type]:
                    print(log)

if __name__ == '__main__':
    file_name_to_summarize = 'example.log'
    def summarizer_impl(file_name_to_summarize):
        summarizer = Summarizer(file_name_to_summarize)
        summarizer.read_log()
        summarizer.visualize_summerize()
    summarizer_impl(file_name_to_summarize)
