# Get Employee's Name
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

# Get Employee's Start Date and End Date   
def GetDatesWorked():
    fromdate = input("Enter From Date (YYYY-MM-DD): ")
    todate = input("Enter To Date (YYYY-MM-DD): ")
    return fromdate, todate

# Get Total Hours Worked By an Employee
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked: '))
    return hours

# Get Hourly Rate of an Employee
def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

# Get Employee's Tax Rate
def GetTaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate

# Calculate Tax and Net Pay 
def CalcTaxAndNetPay(hours,hourlyrate,taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

# Print Employee Details
def printinfo(EmpDetailList):
    
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    
    for EmpList in EmpDetailList:
        
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}",f"{grosspay:,.2f}",f"{taxrate:,.1%}",f"{incometax:,.2f}",f"{netpay:,.2f}")
        
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        
    EmpTotals["TotEmp"] = TotEmployees
    EmpTotals["TotHrs"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay

# Print Total Employee Information
def PrintTotals(EmpTotals):
    
    print()
    print(f"Total Number of Employees: {EmpTotals['TotEmp']}")
    print(f"Total Hours Worked: {EmpTotals['TotHrs']}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total Income Tax: {EmpTotals['TotTax']:,.2f}")
    print(f"Total Net Pay: {EmpTotals['TotNetPay']:,.2f}")

# Write the Employee's Information to the File
def WriteEmployeeInformation(employee):
    
    # open the file in append mode
    file = open("employeeinfo.txt","a")

    # write information separated by pipe
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0],employee[1],employee[2],employee[3],employee[4],employee[5]))

# Get From Date for an Employee
def GetFromDate():
    
    valid = False
    fromdate = ""
    
    # check validity of the date
    while not valid:
        
        fromdate = input("Enter From Date (YYYY-MM-DD): ")
        
        if(len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid Date Format: ")
        else:
            valid = True
    
    return fromdate

# Read the Employee Information from the file and filter by the given date
def ReadEmployeeInformation(fromdate):
    
    EmpDetailList = []
    
    # open the file in read mode
    file = open("employeeinfo.txt","r")
    data = file.readlines()
    
    condition = True
    
    if fromdate.upper() == 'ALL':
        condition = False
    
    for employee in data:
        
        # get employee row
        employee = [x.strip() for x in employee.strip().split("|")]
        
        # append the employee data in the EmpDetailList
        if not condition:
            EmpDetailList.append([employee[0],employee[1],employee[2],float(employee[3]),float(employee[4]),float(employee[5])])
        else:
            if fromdate == employee[0]:
                EmpDetailList.append([employee[0],employee[1],employee[2],float(employee[3]),float(employee[4]),float(employee[5])])
        
    
    return EmpDetailList

if __name__ == "__main__":
    
    EmpDetailList = []
    EmpTotals = {}
    
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        
        print()
    
        # append information to the file
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        WriteEmployeeInformation(EmpDetail)
    
    print()
    print()
    fromdate = GetFromDate()
    
    # Read Employee Information
    EmpDetailList = ReadEmployeeInformation(fromdate)
    
    print()
    printinfo(EmpDetailList)
    
    print()
    PrintTotals(EmpTotals)