#The instance is at the end of the class, there you can send date parameters in these formats.
#La instancia esta al final de la clase, ahi le pueden mandar parametros de fecha en estos formatos.
# 22/05/2016   22/5/2017  22-05-2017  22-5-2017 
#Los ceros a la izquierda no importan pero si el orden dia, mes , año

#coding=utf -8
class AntiquityClass(object):
	def __init__(self):
		self.day_month=[0, 31 , 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		self.months_year = ["", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
		self.leap_year = bool(0) #false
		self.year_1 = 0
		self.month_1 = 0
		self.day_1 = 0
		self.year_2 = 0
		self.month_2 = 0
		self.day_2 = 0


	#METODOS UTILITARIOS
	def getAntiquity(self, date_1, date_2):
		self.date_1=self.getArrayDate(date_1)
		self.date_2=self.getArrayDate(date_2)

		if(self.setDates(self.date_1[0], self.date_1[1], self.date_1[2], self.date_2[0], self.date_2[1], self.date_2[2])):
			if (self.comparationDate()!=bool(1)):
				self.setYearDate1(self.date_2[2])
				self.setMonthDate1(self.date_2[1])
				self.setDayDate1(self.date_2[0])
				self.setYearDate2(self.date_1[2])
				self.setMonthDate2(self.date_1[1])
				self.setDayDate2(self.date_1[0])
				print ("Alerta la segunda fecha es menor que la primera")

			years=self.getDiffYears()
			months=self.getDiffMonth()
			days=self.getDiffDays()

			if (months>=12):
				if (months==12 and self.getDayDate2()<self.getDayDate1()):
					months -= 1
				else:
					months-=12
					years += 1
			if (days >= self.day_month[self.getMonthDate2()]):
				months+=1
				days -= self.day_month[self.getMonthDate1()]

			#Rounding (Days-Months) & (Months-Years)
			if (days >= self.day_month[self.getMonthDate2()]):
				months+=1
				days-=self.day_month[self.getMonthDate2()]
			elif(days>=self.getDayDate1() and (self.getMonthDate1()!=self.getMonthDate2())):
				months+=1
				days-=self.getDayDate1()
			if (months>=12):
				months-=12
				years+=1
			return [days, months, years]
		return ("Fechas Invalidas")


	def setDates(self, day_1, month_1, year_1, day_2, month_2, year_2):
		if (self.validateDate(day_1,month_1,year_1) and self.validateDate(day_2, month_2, year_2)):
			self.setYearDate1(year_1)
			self.setMonthDate1(month_1)
			self.setDayDate1(day_1)
			self.setYearDate2(year_2)
			self.setMonthDate2(month_2)
			self.setDayDate2(day_2)
		else:
			print("Revise las fechas Ingresadas, una o ambas fechas incorrectas")
			return bool(0)
		return bool(1)


	#METODOS PUBLICOS DE LA CLASE FECHA
	def validateDate(self, day, month, year):
		if ((self.validateYear(year) == bool(1)) and (self.validateMonth(month) == bool(1)) and (self.validateDay(day, month) == bool(1))):
			return bool(1)
		else:
			return bool(0)

	def validateYear(self, year):
		if ((year>=1 and year<=9999)!= bool(1)):
			return bool(0)
		if ((year % 4 == 0) and ((year % 100 != 0) or ((year % 100 == 0) and (year % 400 == 0)))):
			self.leap_year = bool(1)
		else:
			self.leap_year = bool(0)
		return bool(1)

	def validateMonth(self, month):
		if ((month>=1 and month<=12)!=bool(1)):
			return bool(0)
		return bool(1)

	def validateDay(self, day, month):
		if (month==2):
			if (self.leap_year==bool(1)):
				if ((day>=1 and day<=29)!=bool(1)):
					return bool(0)
			else:
				if ((day>=1 and day<=28)!=bool(1)):
					return bool(0)
		if (month==4 or month==6 or month==9 or month==11):
			if ((day>=1 and day<=30)!=bool(1)):
				return bool(0)
		if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
			if ((day>=1 and day<=31)!=bool(1)):
				return bool(0)
		return bool(1)


	#METODOS DE DIFERENCIAS ENTRE DOS FECHAS
	def getDiffYears(self):
		diffYears=(self.getYearDate2()-self.getYearDate1())-1
		return diffYears

	def getDiffMonth(self):
		diffMonths=((12 - self.getMonthDate1()) + self.getMonthDate2()) -1
		return diffMonths

	def getDiffDays(self):
		diffDays=(self.day_month[self.getMonthDate1()] - self.getDayDate1()) + self.getDayDate2()
		return diffDays


	#METHODS OF DATA ENTRY
	def setDayDate1(self, day_1):
		self.day_1=day_1

	def setMonthDate1(self, month_1):
		self.month_1=month_1

	def setYearDate1(self, year_1):
		self.year_1=year_1

	def setDayDate2(self, day_2):
		self.day_2=day_2

	def setMonthDate2(self, month_2):
		self.month_2=month_2

	def setYearDate2(self, year_2):
		self.year_2=year_2


	#METHODS OF OBTAINING DATA
	def getDayDate1(self):
		return self.day_1

	def getMonthDate1(self):
		return self.month_1

	def getYearDate1(self):
		return self.year_1

	def getDayDate2(self):
		return self.day_2

	def getMonthDate2(self):
		return self.month_2

	def getYearDate2(self):
		return self.year_2

	#GET DATE ARRANGEMENT FROM A STRING
	def getArrayDate(self, date):
		self.date=date
		if len(self.date.split("-")) == 3:
			array_date = self.date.split("-")
		else:
			array_date = self.date.split("/")
		array_date = [int(i) for i in array_date]
		return array_date

	#METOD COMPARATION DATE
	def comparationDate(self):
		if (self.getYearDate2()>self.getYearDate1()):
			return bool(1)
		elif (self.getYearDate2()==self.getYearDate1()):
			if (self.getMonthDate2()>self.getMonthDate1()):
				return bool(1)
			elif (self.getMonthDate2()==self.getDayDate1()):
				if (self.getDayDate2()>self.getDayDate1()):
					return bool(1)
		return bool(0)

#Instance test
antiquity=AntiquityClass()

#Get Array Antiquity
antiquity_date = antiquity.getAntiquity("28/02/2016","28/02/2017")

#Print Array
print ("Array: ",antiquity_date)

#Get Day
print ("Days: ", antiquity_date[0], "\tMonths: ", antiquity_date[1], "\tYears: ", antiquity_date[2])