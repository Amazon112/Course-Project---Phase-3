#
#
#
from datetime import datetime

FILENAME = "Employees.txt"
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
def GetDatesWorked():
    while True:
        date_str = input("Enter from date (YYYY-MM-DD): ")
        try:
            fromdate = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue  # skip next if statement and re-start loop
        break

    while True:
        date_str = input("Enter to date (YYYY-MM-DD): ")
        try:
            todate = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Try again.")
            print()
        if todate <= fromdate:
            print("To date must be after from date. Try again.")
            print()
        else:
            break    
    return fromdate, todate

def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
#****************************************************************************************************************************
    with open(FILENAME, "r") as Empfile:
        while True:
            rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
            if (rundate.upper() == "ALL"):
                break
            try:
                rundate = datetime.strptime(rundate, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Try again.")
                print()
                continue  # skip next if statement and re-start loop
        while True:
            EmpDetail = EmpFile.readline()
            if not EmpDetail:
                break
            EmpDetail = EmpDetail.replace("\n", "") #remove carriage return from end of line
            EmpList = EmpDetail.split("|")
            fromdate = Emplist[0]
            if (str(rundate).upper() != "ALL"):
                checkdate = datetime.strptime(fromdate, "%Y-%m-%d")
                if (checkdate < rundate):
                    continue
#********************************************************************************************************************************     
            todate = EmpList[1]
            empname = EmpList[2]
            hours = float(EmpList[3])
            hourlyrate  = float(EmpList[4])
            taxrate = float(EmpList[5])
            grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
            print ("********************************************************")
            print("Name:  ", empname) 
            print("Hours Worked: ", f"{hours:,.2f}")
            print("Hourly Rate: ",  f"{hourlyrate:,.2f}")
            print("Gross Pay : ",f"{grosspay:,.2f}")
            print("Tax Rate: ", f"{taxrate:,.1%}")
            print("Income Tax: ",  f"{incometax:,.2f}")
            print("Net Pay: ",  f"{netpay:,.2f}")
            print ("********************************************************")
            print()
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
            DetailsPrinted = True   
        if (DetailsPrinted):  #skip of no detail lines printed
            PrintTotals (EmpTotals)
        else:
            print("No detail information to print")

def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax:  {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')
    
if __name__ == "__main__":

       with open(FILENAME, "a") as Empfile:   #########################################
           #EmpDetailList = []
            EmpTotals = {}
            DetailsPrinted = False
            while True:
                empname = GetEmpName()
                if (empname.upper() == "END"):
                fromdate, todate = GetDatesWorked()
                break
                hours = GetHoursWorked()
                hourlyrate = GetHourlyRate()
                taxrate = GetTaxRate()
                fromdate = fromdate.strftime('%Y-%m-%d')
                todate = todate.strftime('%Y-%m-%d')
                EmpDetail = fromdate + "|" + todate + "|" + empname + "|" + str(hours) + "|" + str(hourlyrate) + "|" + str(taxrate) + "\n"           
                Empfile.write(EmpDetail)                
            Empfile.close()
            printinfo(DetailsPrinted)

#***********************************************************************************************************************************************


