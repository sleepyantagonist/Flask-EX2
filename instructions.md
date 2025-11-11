# Flask Project 1

**Directions:** Download and extract the files from the ZIP folder on Schoology. Move the style.css into the static
folder and the index.html and display.html into the templates folder. Read through the starter code and get a feel for
what this web app will do. If you need further clarification on the starter code, please watch the optional video on
Schoology. Follow the directions listed below to build the interest calculator.

1. Add a new function that routes directly to the display.html template when the Calculate button is pressed on
   the index.html page. Press the button and see if it works.
2. In your new function, modify the decorator and the body to read in data from the POST array. You should set
   local variables for *investment*, *interest_rate*, and *years*. Pass these values through render_template so that they
   can be used in the jinja template display.html. Run you site and see if the data is read into the new
   template correctly.
3. Before we can make our calculations, we need to validate our data! In your display function after you
   read in your data from the POST array, set the *error_message* variable to the following strings based on the data in
   *investment*, *interest_rate*, and *years*. If multiple values are invalid, it is okay for only 1 of the error
   messages to show. If *years* is left empty, set it to 0. (Hint: Don't be afraid to build helper methods!)

> If *investment* is empty: "Investment is a required field."  
> If *investment* is not a number: "Investment must be a valid number."  
> If *investment* is less than or equal to 0: "Investment must be greater than zero."
>
> If *interest_rate* is empty: "Interest rate is a required field."  
> If *interest_rate* is not a number: "Interest rate must be a valid number."  
> If *interest_rate* is less than or equal to 0: "Interest rate must be greater than zero."
>
> If *years* is not a number: "Years must be a valid whole number."  
> If *years* is less than or equal to 0: "Years must be greater than or equal to zero."
>
> If all values are valid: ""

4. Check the value stored in *error_message* if it is not an empty string, render the index.html template passing
   *investment*, *interest_rate*, *years*, and *error_message* through as jinja variables. Test this out. You should see
   the error message showing at the top of the index.html template when rendered. Your form inputs should also *stay*
   populated with the previously submitted data.
5. Final step... the math! Convert your POST data to floats/ints and for each year apply the following formula. Make
   sure to set *value* to the initial investment before you enter your loop. Also, don't forget to set *value* when
   passing parameters to the jinja variables. **Don't forget to round! (Or get fancy and use the string format method to
   always ensure 2 decimal places)**

```python
value = (value + (value * interest_rate * 0.01))
```

## [Example Final Product](https://drive.google.com/file/d/1J_tqsVR5TQ9cTtieZp5ZLsZU6byv_Y4u/view?usp=sharing)


