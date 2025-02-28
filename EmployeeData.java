import java.util.Scanner;

class Employee {
    int empId;
    String depName;
    String empDes;
    String empName;
    String dateJoin;
    double basic;
    double hra;
    double it;
    String desCode;

    public Employee(int empId, String depName, String empDes, String empName, String dateJoin, double basic, double hra, double it, String desCode) {
        this.empId = empId;
        this.depName = depName;
        this.empDes = empDes;
        this.empName = empName;
        this.dateJoin = dateJoin;
        this.basic = basic;
        this.hra = hra;
        this.it = it;
        this.desCode = desCode;
    }
}

public class EmployeeData {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of employees: ");
        int n = sc.nextInt();
        sc.nextLine(); // Consume newline

        Employee[] employees = new Employee[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nEnter details for Employee " + (i + 1) + ":");

            System.out.print("Employee ID: ");
            int empId = sc.nextInt();
            sc.nextLine(); // Consume newline

            System.out.print("Department Name: ");
            String depName = sc.nextLine();

            System.out.print("Employee Designation: ");
            String empDes = sc.nextLine();

            System.out.print("Employee Name: ");
            String empName = sc.nextLine();

            System.out.print("Date of Joining (dd-mm-yyyy): ");
            String dateJoin = sc.nextLine();

            System.out.print("Basic Salary: ");
            double basic = sc.nextDouble();

            System.out.print("House Rent Allowance (HRA): ");
            double hra = sc.nextDouble();

            System.out.print("Income Tax (IT): ");
            double it = sc.nextDouble();
            sc.nextLine(); // Consume newline

            System.out.print("Designation Code: ");
            String desCode = sc.nextLine();

            employees[i] = new Employee(empId, depName, empDes, empName, dateJoin, basic, hra, it, desCode);
        }

        displayEmployeeDetails(employees);
        sc.close();
    }

    private static void displayEmployeeDetails(Employee[] employees) {
        System.out.println("\nEmployee Details:");
        System.out.println("---------------------------------------------------------");
        System.out.printf("%-10s %-15s %-15s %-15s %-15s %-10s %-10s %-10s %-10s\n",
                "EmpID", "Dept Name", "Designation", "Emp Name", "Join Date", "Basic", "HRA", "IT", "Des Code");
        System.out.println("---------------------------------------------------------");

        for (Employee emp : employees) {
            System.out.printf("%-10d %-15s %-15s %-15s %-15s %-10.2f %-10.2f %-10.2f %-10s\n",
                    emp.empId, emp.depName, emp.empDes, emp.empName, emp.dateJoin, emp.basic, emp.hra, emp.it, emp.desCode);
        }
    }
}
