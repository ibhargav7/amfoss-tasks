use std::io;
extern crate regex;
use regex::Regex;

fn main(){
    let mut input = String::new();
    println!("Enter the email ....");
    match io::stdin().read_line(&mut input){
          Ok(_)=>{}
          Err(e)=>println!("invalid {}",e)}
    
    let re = Regex::new(r"\w[[:word:]]+@[[:word:]]+\.[a-zA-Z]").unwrap(); 
    match re.captures(&input) {
           Some(_caps) => println!("valid mail"),
           None => println!("invalid mail")}
}