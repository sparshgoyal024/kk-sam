## About

Execute AWS Lambda for more than 15 minutes without using Step Functions

The function will initially sleep for 895 seconds, that has been put intentionally to making to function execution of 15minutes. Once 895 seconds are over, function will actually execute, and when 899 seconds are over, the function state will be saved in a state file, when this function is executed again, as in real-time this will be automated, the function will resume from the place where it left.

## Instructions

1.  Execute the pre-provision.yaml template to launch an EC2 Instance with all dependencies, and DynamoDB with a Rank Table

2.  Connect to the Instance using EC2 Instance Connect

3.  Once you are in the Terminal, use the below command to provide super user priviledges

    ```sh
    sudo su
    ```

4.  Run the below command to provide AWS Credentials:

    ```sh
    aws configure
    ```

    This command will prompt for credentials.

5.  Execute the below command to initiate a SAM Application

    ```sh
    sam init
    ```
    
    It will prompt for the choice, press 2, as you are using custom template.

5.  When prompted for the application repository, enter below command:

    ```sh
    https://github.com/sparshgoyal024/kk-sam
    ```

18. Once done, use the below command to build the container:

    ```sh
    sam build --use-container
    ```

18. Finally deploy the application using below command:

    ```sh
    sam deploy --guided
    ```

19. When prompted, provide the application details, this step might ask for multiple confirmations.

20. Once done, you will be shown a API URL, execute in the browser, you should get output "Function Execution Successfuly"

21. Navigate to the DynamoDB and Check the Table for the new entries.
