var menu = {
  _courses: {
    appetizers: [],
    mains: [],
    desserts: []
  },
  get appetizers(){
    return this._courses.appetizers
  },
  set appetizers(appetizers){
    this._courses.appetizers = appetizers;
  },
  get mains(){
    return this._courses.mains
  },
  set mains(mains){
    this._courses.mains = mains;
  },
  get desserts(){
    return this._courses.desserts
  },
  set desserts(desserts)
  {
    this._courses.desserts = desserts;
  },
  get courses(){
    return{
      appetizers: this.appetizers,
      mains: this.mains,
      desserts: this.desserts
    }
  },
  addDishToCourse(courseName, dishName, dishPrice)
  {
    var dish = {
      name: dishName,
      price: dishPrice
    };
    this._courses[courseName].push(dish);
  },
  getRandomDishFromCourse(courseName)
  {
    var dishes = this._courses[courseName];
    var num = Math.floor(Math.random() * (dishes.length));
    return dishes[num];
  },
  generateRandomMeal()
  {
    var appetizer = this.getRandomDishFromCourse('appetizers');
    var main = this.getRandomDishFromCourse('mains');
    var dessert = this.getRandomDishFromCourse('desserts');
    const totalPrice = appetizer.price + main.price + dessert.price;

    return `Your meal is ${appetizer.name}, ${main.name}, and ${dessert.name}. The price is $${totalPrice}.`;
  }
}

menu.addDishToCourse('appetizers', 'Tempura Vegetables', 6.50);
menu.addDishToCourse('appetizers', 'Spring Rolls', 6.00);
menu.addDishToCourse('appetizers', 'Crab Legs', 14.00);
menu.addDishToCourse('appetizers', 'Caesar Salad', 4.25);
menu.addDishToCourse('appetizers', 'Fries', 1.25);

menu.addDishToCourse('mains', 'California Rolls', 5.50);
menu.addDishToCourse('mains', 'Crab Sashimi', 13.00);
menu.addDishToCourse('mains', 'Albacore Sushi', 10.00);
menu.addDishToCourse('mains', 'Bruschetta with Salmon', 14.99);
menu.addDishToCourse('mains', 'Lasagna', 10.50);

menu.addDishToCourse('desserts', 'Tiramisu', 10.00);
menu.addDishToCourse('desserts', 'Sesame Cookies', 7.00);
menu.addDishToCourse('desserts', 'Cheesecake', 15.00);
menu.addDishToCourse('desserts', 'Cheesecake', 4.50);
menu.addDishToCourse('desserts', 'Tiramisu', 6.50);

var meal = menu.generateRandomMeal();
console.log(meal);
