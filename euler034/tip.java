//?? how to open the Java Console??

package test_console;


import java.io.Console;
import java.util.Arrays;
public class test {

	public static void main(String[] args) {
		//?? how to open the Java Console??
		Console console = System.console(); 
	    //read user name, using java.util.Formatter syntax :
	    String username = console.readLine("User Name? ");

	    //read the password, without echoing the output 
	    char[] password = console.readPassword("Password? ");

	    //verify user name and password using some mechanism (elided)

	    //the javadoc for the Console class recommends "zeroing-out" the password 
	    //when finished verifying it :
	    Arrays.fill(password, ' ');

	    console.printf("Welcome, %1$s.", username);
	    console.printf(fNEW_LINE);

	    String className = console.readLine("Please enter a package-qualified class name:");
	    Class theClass = null;
	    try {
	      theClass = Class.forName(className);
	      console.printf("The inheritance tree: %1$s", getInheritanceTree(theClass));
	    }
	    catch(ClassNotFoundException ex){
	      console.printf("Cannot find that class.");
	    }

	    //this version just exits, without asking the user for more input
	    console.printf("Bye.");
	}
	
	// PRIVATE
	  private static final String fNEW_LINE = System.getProperty("line.separator");

	  private static String getInheritanceTree(Class aClass){
	    StringBuilder superclasses = new StringBuilder();
	    superclasses.append(fNEW_LINE);
	    Class theClass = aClass;
	    while (theClass != null) {
	      superclasses.append(theClass);
	      superclasses.append(fNEW_LINE);
	      theClass = theClass.getSuperclass();
	    }
	    superclasses.append(fNEW_LINE);
	    return superclasses.toString();
	  }

}