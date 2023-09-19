# ATM Management System

![ATM Management System](link_to_project_image)

## Project Description

The ATM Management System is a personal project aimed at simulating the functionality of an Automated Teller Machine (ATM). This Java program includes two main classes: `BankAccount` and `User`.

### Features

- **User-Friendly GUI:** The program features a graphical user interface (GUI) that interacts with the user to provide a seamless ATM experience.

- **PIN Validation:** Users are prompted to enter a Personal Identification Number (PIN) to access their accounts securely. Incorrect PIN entries can be cleared, and the program requests the correct PIN.

- **Account Menu:** After successful login, the program displays the user's name and a menu with multiple options, including checking account balance, withdrawing money, depositing money, and transferring money to another account.

### Usage

1. **PIN Entry:** Upon launching the program, users are greeted with the message "Please insert your card and press ENTER." Once the ENTER button is pressed, they are prompted to enter their PIN.

2. **Account Menu:** After entering the correct PIN, users see a menu where they can choose various options:
   - **OPTION 1 (Check Balance):** Displays the user's name and account balance. Pressing ENTER returns to the PIN entry screen.
   - **OPTION 2 (Withdraw Money):** Allows users to enter the amount they want to withdraw. If the entered amount exceeds the account balance, an error message is shown.
   - **OPTION 3 (Deposit Money):** Prompts users to enter the amount they want to deposit.
   - **OPTION 4 (Transfer Money):** Initiates a money transfer. Users enter the receiver's account number, and the system validates it. Then, users input the amount to transfer, and successful transfers are confirmed.

3. **Error Handling:** The system handles various error scenarios, such as incorrect PIN entries, insufficient account balance for withdrawals or transfers, and incorrect receiver account numbers for transfers.

4. **Cancellation:** At any point during an operation, users can cancel by pressing the CANCEL button.

Please note that the language buttons are for design purposes and are not implemented as part of this project.

### Technologies Used

- Java
- Java Swing (for GUI)
- IntelliJ IDEA (Development Environment)

### Installation

To run the ATM Management System on your local machine:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/atm-management-system.git
