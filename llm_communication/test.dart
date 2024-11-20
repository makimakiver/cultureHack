import 'dart:convert';
import 'dart:io';

/// A Dart application to interact with a Python script that retrieves
/// culturally significant information based on user preferences and region.
///
/// Usage:
///   dart main.dart "<userPreferences>" "<region>"
///
/// Example:
///   dart main.dart "interest in history and festivals" "Kyoto"

Future<void> main(List<String> arguments) async {
  // Check if the correct number of arguments are provided
  if (arguments.length < 2) {
    print('Usage: dart main.dart "<userPreferences>" "<region>"');
    exit(1);
  }

  // Extract user preferences and region from command-line arguments
  String userPreferences = arguments[0];
  String region = arguments[1];

  // Path to the Python script
  // If the Python script is in the same directory, you can use:
  // String pythonScript = 'get_culture.py';
  // Otherwise, provide the absolute or relative path.
  String pythonScript = 'get_culture.py';

  // Optional: Specify the Python executable if not in PATH
  // For example, on Windows:
  // String pythonExecutable = 'python.exe';
  // On Unix/Linux/macOS:
  // String pythonExecutable = 'python3';
  String pythonExecutable = 'python.exe'; // Adjust if necessary

  try {
    // Execute the Python script with the provided arguments
    ProcessResult result = await Process.run(
      pythonExecutable,
      [pythonScript, userPreferences, region],
      // You can set the current working directory if needed
      // workingDirectory: '/path/to/script/',
      // Optionally, set environment variables
      // environment: {'OPENAI_API_KEY': 'your_api_key'},
    );

    // Check if the Python script executed successfully
    if (result.exitCode != 0) {
      stderr.writeln('Error executing Python script:');
      stderr.writeln(result.stderr);
      exit(result.exitCode);
    }

    // The Python script prints the output to stdout
    String output = result.stdout.trim();

    // Optionally, process the output (e.g., parse JSON if applicable)
    // For now, we'll just print it
    print('Cultural Information for "$region":\n$output');
  } catch (e) {
    stderr.writeln('An error occurred while running the Python script: $e');
    exit(1);
  }
}



