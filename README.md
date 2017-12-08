## References
  http://www.oodesign.com/ <br>
  https://www.tutorialspoint.com/design_pattern/design_pattern_overview.htm <br>
  https://www.codeproject.com/Articles/98598/How-I-explained-Design-Patterns-to-my-wife-Part <br>
  https://code.tutsplus.com/articles/a-beginners-guide-to-design-patterns--net-12752 <br>
  https://app.pluralsight.com/library/courses/python-design-patterns/table-of-contents <br>
  https://app.pluralsight.com/library/courses/python-design-patterns-building-more/table-of-contents <br>
  
  

## Behavioral Pattern
	Strategy/Policy Pattern 
		Family of algorithms, switch among them), different classes implementing same abstract method interface		
		ex : (Shipping Cost(FedexStrategy, UPSStrategy)
	
	Observer/Publisher-Subscriber/Dependents Pattern 
		for Event Monitoring
		Define 1-Many relation among set of objects, so when state of 1 changes, others are notified)]
		ex : Dashboard KPIs of some subject gets updated on changes to subject

	Command/Action/Transaction Pattern
		Encapsulate request as an object
		ex : cmd line args parsing handlers
		
	Template Method Pattern(Equivalent Algos)
		defines algo skeleton
		ex : prepare_rice_item()--------->Template Method(Order of function call is defined)
				prepare_spices()--------->@abstractmethod
				make_rice()-------------->concrete method
				mix_rice()--------------->concrete method
	
		Similarily in BuilderPattern : BUT Construction of Objects
		
## Creational Pattern
	Singleton Pattern(Ensure a class has only 1 instance), control access to limited resource
		To control access to instances of a class
		Object-Oriented way of handling global state
		global point of access, use it sparingly, it is considered as AntiPattern by many
		ex : Logging , one instance to write to file
	
	Builder Pattern(Create complex objects)
		Encapsulate construction of object
		Multi-step construction process
		ex : Custom Computer Builder
		ctor with many arguments, encapsulate its creation in another abstract class, who's concrete methods provide differnt versions
		
	Factory/Virtual Constructor Pattern(Create different object through an API)
		define an interface for creating an object
		let subclasses decide which object to create
		defer instantiation to subclasses
		
		Factory that create a single product
			Single Factory(auto create and load objects in a auto_factory)
				ex : Local Dealer can sell basic model of different automobiles
			Multiple Factories(auto create and load objects via their factories)
				ex : Kalyani Dealer can sell basic model of Maruti Cars
				     Mahindra- Dealer can sell basic model of Renault Cars
		Factory that create a family of products
			Abstract Factory/Kit Pattern(create family of related or dependant objects without specfying concrete classes)
				ex : Kalyani Dealer can sell basic and premium models of Maruti Cars

	None Pattern (to avoid None test), Provides a Default Object

## Structural Pattern
	Facade Pattern(Present Unified High level interface to a set of interfaces)
		ex : get data from different databases(ConnectionManager)
	
	Adapter/Wrapper Pattern(Converts interface of a class)
		types:
		1. Object Adapter : Composition
			ex:Customer(Name,Address), Vendor(Name, Street, City, PostalCode)
		2. Class Adapter : Inheritance 
	
	Adapter/Wrapper : Combat incompatiple APIs
	Decorator/Wrapper : Add new responsibilities
	
	Decorator/Wrapper Pattern(Add responsibility at run time instaed of complile time, avoiding so many subclasses)
		ex:For a Car Object add decorations 1-by-1 incresing car cost
	
	


