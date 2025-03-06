# Secret Hitler

This project is CLI version of the game Secret Hitler.

## Setting Up Bazel

To build and run this project, you need to have Bazel installed on your system. Follow these steps to set up Bazel:

1. **Download and Install Bazel**:
   - Visit the [Bazel releases page](https://github.com/bazelbuild/bazel/releases) to download the installer for your operating system.
   - Download version `8.1.1` for consistency.
   - Follow the installation instructions specific to your OS.

2. **Verify Installation**:
   - Open a terminal and run the following command to verify that Bazel is installed correctly:
     ```bash
     bazel --version
     ```
   - This should display the installed version of Bazel.

3. **Add Bazel to PATH** (if necessary):
   - Ensure that the directory containing `bazel.exe` is included in your system's PATH environment variable.
   - On Windows, you can add the path by going to `System Properties` > `Environment Variables` and editing the `Path` variable.
   - On Windows, based on how VS Code is setup, you might need to add below snippet in `settings.json`, for bazel to work.
        ```
        "terminal.integrated.env.windows": {
            "PATH": "<path_to_bazel_exe>;${env:PATH}"
        }
        ```

## Building and Running `hello_world` 

Once Bazel is set up, you can build and run the `hello_world` program:

1. **Navigate to the Project Directory**:
   - Open a terminal and navigate to the root of the project directory:
     ```bash
     cd path/to/secret-hitler-game
     ```

2. **Build the Program**:
   - Use Bazel to build the `hello_world` target:
     ```bash
     bazel build //src:hello_world
     ```

3. **Run the Program**:
   - After building, run the program using the following command:
     ```bash
     ./bazel-bin/src/hello_world
     ```
   - You should see the output:
     ```
     Hello, World!
     ```

## Directly Running `hello_world`

Once Bazel is set up, you can build and run the `hello_world` program:

1. **Navigate to the Project Directory**:
   - Open a terminal and navigate to the root of the project directory:
     ```bash
     cd path/to/secret-hitler-game
     ```

2. **Run the bazel target**:
   - Use Bazel to build & run the `hello_world` target:
     ```bash
     bazel run //src:hello_world
     ```

By following these steps, you can set up Bazel and run the `hello_world` program successfully. If you encounter any issues, please refer to the Bazel documentation or reach out for support.