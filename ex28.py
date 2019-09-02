Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:\Users\Cecilia\Desktop\ex24.py =================
Let's practice everything.
You'd need to know 'boout escapes with \ that do:

 newlines and 	 tabs.
-----------

	The lovely world
with logic so firmly planted
cannot discer 
 the needs of love
nor comprehend passion from intuition
and requires an explanation

	 where there is none.

-----------
This should be five: 5
With a starting point of: 1000
We'd have 500000 beans, 500.0 jars, and 5.0 crates.
We can also do that this way:
We'd have 50000.0 beans, 50.0 jars, and 0.5 crates.
>>> 
================= RESTART: C:/Users/Cecilia/Desktop/ex28.py =================
Traceback (most recent call last):
  File "C:/Users/Cecilia/Desktop/ex28.py", line 1, in <module>
    true and true
NameError: name 'true' is not defined
>>> 
================= RESTART: C:/Users/Cecilia/Desktop/ex28.py =================
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> True and True
True
>>> False and True
False
>>> 1 ==1 and 2==1
False
>>> "test" == "testing"
False
>>> 1 == 1 or 2!1
SyntaxError: invalid syntax
>>> 1 == 1 or 2!=1
True
>>> True and 1==1
True
>>> False and 0!=0
False
>>> True or 1==1
True
>>> "test"== "testing"
False
>>> 1 ! 0 and  2==1
SyntaxError: invalid syntax
>>> 1!=0 and 2==1
False
>>> "test" != "testing"
True
>>> "test" ==1
False
>>> not(True and False)
True
>>> not( 1==1 and 0!= 1)
False
>>> not(10 == 1 or 1000 ==1000)
False
>>> not(1 != 10 0r 3==4)
SyntaxError: invalid syntax
>>> not(1 !=10 or 3==4)
False
>>> not ("testing" == "testing" and "Zed" == "Cool Guy")
True
>>> 1 ==1 and (not("testing" ==1 or 1==0))
True
>>> "chunky" == "bacon" and (not(3 == 4 or 3==3))
False
>>> 3 == 3 and (not("testing" == "testing" or "Python" == "Fun"))
False
>>> 
