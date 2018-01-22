from gss import psyQuery as qry

def cleanPhoneNumbers(strTable,strPhone):
    L1 = """update "{}" set {} = replace({}, '+', '');\n""".format(strTable,strPhone,strPhone)
    L2 = """update "{}" set {} = replace({}, '(', '');\n""".format(strTable,strPhone,strPhone)
    L3 = """update "{}" set {} = replace({}, ')', '');\n""".format(strTable,strPhone,strPhone)  
    L4 = """update "{}" set {} = replace({}, '-', '');\n""".format(strTable,strPhone,strPhone) 
    L5 = """update "{}" set {} = replace({}, ' ', '');\n""".format(strTable,strPhone,strPhone)
    L6 = """update "{}" set {} = \n""".format(strTable,strPhone)
    L7="""    case when Length("{}") = 10 Then      /* '(123) 456-7890'*/\n""".format(strPhone)
    L8="""	concat( "(" , left("{}", 3) , ") " , substring("{}", 4, 3) , "-" , right("{}", 4))\n""".format(strPhone,strphone,strPhone)
    L9=""" 	when left("{}",3)="613" then\n""".format(strPhone)
    L10="""concat( "(" , left("{}", 3) , ") " , substring("{}", 4, 3) , "-" , substring("{}",7, 4), right("{}",11))\n""".format(strPhone,strPhone,strPhone,strPhone)
    L11="""	when  Length("{}") = 12 Then     /* '0123 12 34 5678', '0123 12 34 5678 x90123' */\n""".format(strPhone)
    L12="""        	concat( "+" , left("{}", 4) , " " , substring("{}", 5, 4) , " " , right("{}", 4))\n""".format(strPhone,strPhone,strPhone)
    L13=""" when Length("{}") = 14 then          /* '0123 4563 78 9012' */\n""".format(strPhone)
    L14="""   	concat( "+" & left("{}", 4) , " " , substring("{}", 3, 2) , " " , substring("{}", 6, 4) , "-" , right("{}", 4))\n""".format(strPhone,strPhone,strPhone,strPhone)
    L15="""	when Length("{}") > 4 then     /*'01234567891'*/\n""".format(strPhone)
    L16="""        	concat(left("{}", Length("{}") - 4) , "-" , right("{}", 4))\n""".format(strPhone,strPhone,strPhone)
    L17="""    	else\n"""
    L18="""        	"{}"\n""".format(strPhone)
    L19="""    	end;\n"""

    strQuery = L1+L2+L3+L4+L5+L6+L7+L8+L9+L10+L11+L12+L13+L14+L15+L16+L17+L18+L19

    qry(strQuery)

