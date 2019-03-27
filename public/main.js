var ingredientName = document.getElementById("ingredient_name");
var ingredientAmount = document.getElementById("ingredient_amount");
var ingredientAllergy1 = document.getElementById("ingredient_allergy1");
var ingredientAllergy2 = document.getElementById("ingredient_allergy2");
var ingredientAllergy3 = document.getElementById("ingredient_allergy3");
var ingredientAllergy4 = document.getElementById("ingredient_allergy4");
var ingredientAllergy5 = document.getElementById("ingredient_allergy5");
var ingredients = [];

$(document).ready(function(){
    $("#add_ingredient_data").on("click", function() {
        console.log("works so far");
        if(ingredientName.value == 0){
            return alert("Ingredient Name field empty");
        } 
        if (ingredientAmount.value == 0){
            return alert("Ingredient Amount field empty");
        }
        var ingredientData = new Object();
        ingredientData.ingredient_name = ingredientName.value;
        ingredientData.ingredient_amount = ingredientAmount.value;
        ingredientData.ingredient_allergies = [];
            
        var addAllergy = function(v){
            if(v.value > 0){
                var content = v.value;
                ingredientData.ingredient_allergies.push(content);
            }
        }
        addAllergy(ingredientAllergy1);
        addAllergy(ingredientAllergy2);
        addAllergy(ingredientAllergy3);
        addAllergy(ingredientAllergy4);
        addAllergy(ingredientAllergy5);
        ingredients.push(ingredientData);
        $("#ingredients").append("added");
    });
    //https://stackoverflow.com/questions/53694709/passing-javascript-array-in-python-flask
    $("#save_recipe").on("click", function() {
        var js_data = JSON.stringify(ingredients.splice());
        console.log(js_data);
        $.ajax({                        
            url: '/insert_recipe',
            type : 'post',
            contentType: 'application/json',
            dataType : 'json',
                data : js_data
            }).done(function(result) {
                console.log("done")
            }).fail(function(jqXHR, textStatus, errorThrown) {
                console.log("fail: ",textStatus, errorThrown);
            });
        });
    });
});
