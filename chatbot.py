"""
============================================================
  Login & Dashboard System - CMD Chatbot
  Serves Java code snippets from the README documentation.
============================================================
"""

COMMANDS = {
    "help": "List all available commands",
    "dbconnect": "Show DBConnect.java - MySQL connection class",
    "btnlogin": "Show Login button action (btnLoginActionPerformed)",
    "btnexit": "Show Exit button action (btnExitActionPerformed)",
    "btnsignup": "Show Signup button action (btnSignupActionPerformed)",
    "admindash": "Show Admin Dashboard constructor (dashboard.java)",
    "userdash": "Show User Dashboard constructor (udashboard.java)",
    "btnregister": "Show Register button action (btnRegisterActionPerformed)",
    "btnback": "Show Back button action (btnBackActionPerformed)",
    "list": "List all Java files/sections in the documentation",
    "clear": "Clear the screen",
    "exit": "Exit the chatbot",
}

JAVA_CODE = {

    "dbconnect": {
        "title": "DBConnect.java — MySQL Connection Class",
        "file": "DBConnect.java",
        "code": """\
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DBConnect {
    private static final String URL = "jdbc:mysql://localhost:3306/login_db";
    private static final String USER = "root";
    private static final String PASS = "";

    public static Connection getConnection(){
        try {
            return DriverManager.getConnection(URL, USER, PASS);
        } catch(SQLException e) {
            e.printStackTrace();
            return null;
        }
    }
}"""
    },

    "btnlogin": {
        "title": "Login Form — btnLoginActionPerformed",
        "file": "LoginForm.java",
        "note": "Fields: uname (username), upass (password)",
        "code": """\
private void btnLoginActionPerformed(java.awt.event.ActionEvent evt) {
    String username = uname.getText().trim();
    String password = String.valueOf(upass.getPassword()).trim();

    if (username.isEmpty() || password.isEmpty()) {
        JOptionPane.showMessageDialog(this, "Please fill all fields");
        return;
    }

    // Updated SQL to get role, fname, and lname
    String sql = "SELECT role, fname, lname FROM users WHERE username = ? AND password = ?";

    try (java.sql.Connection con = DBConnect.getConnection()) {
        if (con == null) {
            JOptionPane.showMessageDialog(this, "Database Connection Failed!");
            return;
        }

        try (java.sql.PreparedStatement ps = con.prepareStatement(sql)) {
            ps.setString(1, username);
            ps.setString(2, password);

            try (java.sql.ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    // Get role and names
                    String role = rs.getString("role").trim();
                    String fname = rs.getString("fname").trim();
                    String lname = rs.getString("lname").trim();

                    System.out.println("Role: [" + role + "], Name: [" + fname + " " + lname + "]");

                    if (role.equalsIgnoreCase("Admin")) {
                        // Redirect to admin dashboard and pass names
                        dashboard adminDash = new dashboard(fname, lname);
                        adminDash.setLocationRelativeTo(null);
                        adminDash.setVisible(true);
                        this.dispose();
                    } else if (role.equalsIgnoreCase("User")) {
                        // Redirect to user dashboard and pass names
                        udashboard userDash = new udashboard(fname, lname);
                        userDash.setLocationRelativeTo(null);
                        userDash.setVisible(true);
                        this.dispose();
                    } else {
                        JOptionPane.showMessageDialog(this, "Unknown role. Contact admin.");
                    }
                } else {
                    JOptionPane.showMessageDialog(this, "Invalid Username or Password");
                }
            }
        }
    } catch (Exception e) {
        JOptionPane.showMessageDialog(this, "Database Error: " + e.getMessage());
        e.printStackTrace();
    }
}"""
    },

    "btnexit": {
        "title": "Login Form — btnExitActionPerformed",
        "file": "LoginForm.java",
        "code": """\
private void btnExitActionPerformed(java.awt.event.ActionEvent evt) {
    int choice = JOptionPane.showConfirmDialog(
        this,
        "Are you sure you want to exit?",
        "Exit Confirmation",
        JOptionPane.YES_NO_OPTION,
        JOptionPane.QUESTION_MESSAGE
    );
    if (choice == JOptionPane.YES_OPTION) {
        System.exit(0);
    }
}"""
    },

    "btnsignup": {
        "title": "Login Form — btnSignupActionPerformed",
        "file": "LoginForm.java",
        "code": """\
private void btnSignupActionPerformed(java.awt.event.ActionEvent evt) {
    Signup sg = new Signup();
    sg.setLocationRelativeTo(null);
    sg.setVisible(true);
    this.dispose();
}"""
    },

    "admindash": {
        "title": "Admin Dashboard Constructor — dashboard.java",
        "file": "dashboard.java",
        "note": "Labels: lblWelcome, time",
        "code": """\
public dashboard(String fname, String lname) {
    initComponents();
    lblWelcome.setText("Welcome, " + fname + " " + lname);
    javax.swing.Timer timer = new javax.swing.Timer(1000, e -> {
        java.time.LocalDateTime now = java.time.LocalDateTime.now();
        java.time.format.DateTimeFormatter formatter = java.time.format.DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        time.setText(now.format(formatter));
    });
    timer.start();
}"""
    },

    "userdash": {
        "title": "User Dashboard Constructor — udashboard.java",
        "file": "udashboard.java",
        "note": "Labels: lblWelcome, time",
        "code": """\
public udashboard(String fname, String lname) {
    initComponents();
    lblWelcome.setText("Welcome, " + " " + lname);
    javax.swing.Timer timer = new javax.swing.Timer(1000, e -> {
        java.time.LocalDateTime now = java.time.LocalDateTime.now();
        java.time.format.DateTimeFormatter formatter = java.time.format.DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        time.setText(now.format(formatter));
    });
    timer.start();
}"""
    },

    "btnregister": {
        "title": "Signup Form — btnRegisterActionPerformed",
        "file": "Signup.java",
        "note": "Fields: uname, upass, fname, mname, lname, urole",
        "code": """\
private void btnRegisterActionPerformed(java.awt.event.ActionEvent evt) {
    String username = uname.getText().trim();
    String password = String.valueOf(upass.getPassword()).trim();
    String firstname = fname.getText().trim();
    String middlename = mname.getText().trim();
    String lastname = lname.getText().trim();
    String role = urole.getSelectedItem().toString();

    if (username.isEmpty() || password.isEmpty()) {
        JOptionPane.showMessageDialog(this, "Fill all fields");
        return;
    }

    String sql = "INSERT INTO users(username, password, fname, mname, lname, role) VALUES(?,?,?,?,?,?)";

    try (java.sql.Connection con = DBConnect.getConnection();
         java.sql.PreparedStatement ps = con.prepareStatement(sql)) {

        if (con == null) {
            JOptionPane.showMessageDialog(this, "Database connection failed!");
            return;
        }

        ps.setString(1, username);
        ps.setString(2, password);
        ps.setString(3, firstname);
        ps.setString(4, middlename);
        ps.setString(5, lastname);
        ps.setString(6, role);

        int rowsInserted = ps.executeUpdate();

        if (rowsInserted > 0) {
            JOptionPane.showMessageDialog(this, "Registration Successful!");

            Login login = new Login();
            login.setLocationRelativeTo(null);
            login.setVisible(true);
            this.dispose();

            // Clear fields after successful registration
            uname.setText("");
            upass.setText("");
            fname.setText("");
            mname.setText("");
            lname.setText("");
            urole.setSelectedIndex(0);
        } else {
            JOptionPane.showMessageDialog(this, "Registration Failed!");
        }
    } catch (Exception e) {
        e.printStackTrace();
        JOptionPane.showMessageDialog(this, "Error Saving Data: " + e.getMessage());
    }
}"""
    },

    "btnback": {
        "title": "Signup Form — btnBackActionPerformed",
        "file": "Signup.java",
        "code": """\
private void btnBackActionPerformed(java.awt.event.ActionEvent evt) {
    Login log = new Login();
    log.setVisible(true);
    this.dispose();
}"""
    },
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def separator(char="─", width=62):
    print(char * width)

def header(text):
    separator("═")
    print(f"  {text}")
    separator("═")

def print_code(entry):
    header(entry["title"])
    if "file" in entry:
        print(f"  📄 File : {entry['file']}")
    if "note" in entry:
        print(f"  📝 Note : {entry['note']}")
    separator()
    print(entry["code"])
    separator()
    print()

def cmd_help():
    header("AVAILABLE COMMANDS")
    max_len = max(len(k) for k in COMMANDS)
    for cmd, desc in COMMANDS.items():
        print(f"  {cmd:<{max_len + 2}}  {desc}")
    separator()
    print()

def cmd_list():
    header("JAVA FILES IN DOCUMENTATION")
    sections = [
        ("DBConnect.java",  ["dbconnect"]),
        ("LoginForm.java",  ["btnlogin", "btnexit", "btnsignup"]),
        ("dashboard.java",  ["admindash"]),
        ("udashboard.java", ["userdash"]),
        ("Signup.java",     ["btnregister", "btnback"]),
    ]
    for file, cmds in sections:
        print(f"  📄 {file}")
        for c in cmds:
            print(f"       → {c}  ({JAVA_CODE[c]['title'].split('—')[-1].strip()})")
    separator()
    print()

def cmd_clear():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def welcome():
    separator("═")
    print("  Login & Dashboard System — Java Code Assistant")
    print("  Type  help  to see all commands,  exit  to quit.")
    separator("═")
    print()


# ── Main Loop ─────────────────────────────────────────────────────────────────

def main():
    welcome()
    while True:
        try:
            raw = input("chatbot> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        cmd = raw.lower()

        if not cmd:
            continue
        elif cmd == "exit":
            print("Goodbye!")
            break
        elif cmd == "help":
            cmd_help()
        elif cmd == "list":
            cmd_list()
        elif cmd == "clear":
            cmd_clear()
            welcome()
        elif cmd in JAVA_CODE:
            print_code(JAVA_CODE[cmd])
        else:
            # Fuzzy hint: suggest closest command
            matches = [k for k in list(COMMANDS.keys()) + list(JAVA_CODE.keys()) if cmd in k]
            print(f"  ❌ Unknown command: '{cmd}'")
            if matches:
                print(f"  💡 Did you mean: {', '.join(matches)}")
            else:
                print("  Type  help  to see all available commands.")
            print()


if __name__ == "__main__":
    main()
