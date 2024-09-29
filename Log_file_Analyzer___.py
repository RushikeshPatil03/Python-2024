#Program on log file analyzer
from datetime import datetime
from collections import defaultdict

class LogEntry:
    def __init__(self, timestamp, log_level, message):
        self.timestamp = timestamp
        self.log_level = log_level
        self.message = message

    def to_string(self):
        return f"{self.timestamp} [{self.log_level}] {self.message}"

class LogFileAnalyzer:
    def __init__(self):
        self.logs = []

    def create_log(self, log_level, message):
        timestamp = datetime.now().isoformat()
        log_entry = LogEntry(timestamp, log_level, message)
        self.logs.append(log_entry)

    def read_logs(self):
        return [log.to_string() for log in self.logs]

    def update_log(self, index, log_level, message):
        if 0 <= index < len(self.logs):
            self.logs[index].log_level = log_level
            self.logs[index].message = message
            return True
        return False

    def delete_log(self, index):
        if 0 <= index < len(self.logs):
            del self.logs[index]
            return True
        return False

    def analyze_logs(self):
        error_counts = defaultdict(int)
        for log in self.logs:
            if log.log_level == "ERROR":
                error_counts[log.message] += 1
        return dict(error_counts)

    def summarize_logs(self):
        summary = {
            'total_entries': len(self.logs),
            'error_count': sum(1 for log in self.logs if log.log_level == "ERROR"),
            'warning_count': sum(1 for log in self.logs if log.log_level == "WARNING"),
        }
        return summary

    def export_logs(self, filename):
        with open(filename, 'w') as f:
            for log in self.logs:
                f.write(log.to_string() + '\n')

    def import_logs(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    timestamp, rest = line.split(' [', 1)
                    log_level, message = rest.split('] ', 1)
                    self.logs.append(LogEntry(timestamp, log_level.strip(), message.strip()))
        except Exception as e:
            print(f"Error importing logs: {e}")

# Example usage
if __name__ == "__main__":
    analyzer = LogFileAnalyzer()

    while True:
        print("\nMenu:")
        print("1: Create logs")
        print("2: Read logs")
        print("3: Update logs")
        print("4: Delete logs")
        print("5: Analyze logs")
        print("6: Summarize logs")
        print("7: Export logs")
        print("8: Import logs")
        print("0: Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            log_level = input("Enter log level (INFO, WARNING, ERROR): ")
            message = input("Enter log message: ")
            analyzer.create_log(log_level, message)

        elif choice == '2':
            print("\nLog Entries:")
            for log in analyzer.read_logs():
                print(log)

        elif choice == '3':
            index = int(input("Enter log index to update: "))
            log_level = input("Enter new log level: ")
            message = input("Enter new log message: ")
            if analyzer.update_log(index, log_level, message):
                print("Log updated successfully.")
            else:
                print("Invalid index.")

        elif choice == '4':
            index = int(input("Enter log index to delete: "))
            if analyzer.delete_log(index):
                print("Log deleted successfully.")
            else:
                print("Invalid index.")

        elif choice == '5':
            print("\nError Analysis:")
            error_analysis = analyzer.analyze_logs()
            print(error_analysis)

        elif choice == '6':
            print("\nLog Summary:")
            summary = analyzer.summarize_logs()
            print(summary)

        elif choice == '7':
            filename = input("Enter filename to export logs: ")
            analyzer.export_logs(filename)
            print("Logs exported successfully.")

        elif choice == '8':
            filename = input("Enter filename to import logs: ")
            analyzer.import_logs(filename)
            print("Logs imported successfully.")

        elif choice == '0':
            print("\nGoodbye!")
            break
        else:
            print("Invalid option.")
