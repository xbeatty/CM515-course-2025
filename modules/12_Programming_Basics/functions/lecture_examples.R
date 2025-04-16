#slide 6 ------ functions you've already been using 

calc_conc <- function(absorbance) {
  return(absorbance*1.45)
}


typeof(calc_conc) #?

typeof(calc_conc(80)) #?

typeof(calc_conc()) #?

























# Slide 8 ------  local and Global scope demo
# Let’s say you're calculating total DNA mass from concentration and volume:

calc_dna_mass <- function(concentration_ng_per_uL, volume_uL) {
  mass <- concentration_ng_per_uL * volume_uL
  return(mass)
}

calc_dna_mass(50, 20)






#without an argument 
greet <- function() {
  return("Hello, CM515 students!")
}


















# with argument
greet <- function(name) {
  message <- paste("Hello,", name)
  return(message)
}




















# setting default 
greet <- function(name = "CM515 Students") {
  message <- paste("Hello,", name)
  return(message)
}












# Slide 9 ------  local and Global scope demo
#example 1 -- local variable
calculate_protein_mass <- function(concentration, volume) {
  protein_mass <- concentration * volume  # 'mass' exists only here
  return(protein_mass)
}
calculate_protein_mass(10, 2)

paste(protein_mass)

















#example 2 -- global variable
mass <- 100
paste("global mass is:", mass)

calculate_protein_mass <- function(concentration, volume) {
  mass <- concentration * volume
  print(paste("local mass is:", mass))
  return(mass)
}

calculate_protein_mass(2, 5)
paste("global mass is still:", mass)

















# Slide 10 ------ control flow in functions
is_positive <- function(x) {
  if (x > 0) {
    return("Positive")
  } else {
    return("Not positive")
  }
}
is_positive(-2)














# improve this function to account for non-numeric inputs and NA argument
classify_number <- function(x) {
  if (x > 0) {
    return("Positive")
  } else if (x < 0) {
    return("Negative")
  } else {
    return("Zero")
  }
}

classify_number()


















#Let's say you have a vector of protein concentrations from multiple samples, 
#and you want to flag which ones are below a minimum threshold (e.g., 20 ng/µL).

flag_low_proteins <- function(concentrations, threshold = 20) {
  
  
}

protein_samples <- c(10, 25, 18, 30)
flag_low_proteins(protein_samples)
# Output: "LOW" "OK" "LOW" "OK"















# Slide 11 --  Functions with multiple conditions
# Example 1
grade_student <- function(score) {
  if (score >= 90) {
    return("A")
  } else if (score >= 80) {
    return("B")
  } else if (score >= 70) {
    return("C")
  } else if (score >= 60) {
    return("D")
  } else {
    return("F")
  }
}

scores <- c(95, 83, 72, -98, 105, 64)




#example 2, complete this function to use a for loop 
grade_student <- function(scores) {
  
}

scores <- c(95, 83, 72, NA, -5, 105, 64)
grade_student(scores)








# Slide 12 --  what does out look like at each stage if we call double_values(c(1,3,8))?
double_values <- function(vec) {
  out <- c()                    # Step 1: initialize an empty vector
  for (val in vec) {            # Step 2: loop through each element in input vector
    out <- c(out, val * 2)      # Step 3: double the value and append it to `out`
  }
  return(out)                   # Step 4: return final result
}

# before for-loop execution out is: simply c()
# first iteration:
# second iteration:
# third iteration: 
#return: 









# Slide 13 --  what does out look like at each stage if we call double_values(c(1,3,8))?
custom_mean <- function(x, ...) {
  mean(x, ...)
}
custom_mean(c(1, 2, 3, 4, NA))












#### how many functions are in this block ?
library(ggplot2)

df <- data.frame(
  group = c("A", "B", "C"),
  value = c(4, 7, 2)
)

ggplot(df, aes(x = group, y = value)) +
  geom_col(fill = "steelblue") +
  labs(title = "Bar Plot", x = "Group", y = "Value") +
  theme_minimal()


