  $(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('select').formSelect();
    $('.chips').chips();
  });

// Add and remove ingredients and instruction steps in new recipe form, Solution by deevdz on Github adapted for this project
var ingredientField = '<div class ="new-ingredient"><div class="input-field col s11"><input type="text" name="ingredients" class="validate" required><label for="ingredients" class="white-text">Another ingredient</label></div><div class="col s1"><a class="btn-small waves-effect grey lighten-3 light-green-text rounded-element center-align" id="remove_ingredient"><i class="fas fa-minus-square"></i></a></div></div>';
var stepField = '<div class="new-instruction-step"><div class="input-field col s11"><input type="text" name="instructions" class="validate" required><label for="instructions" class="white-text">Instructions</label></div><div class="col s1"><a class="btn-small waves-effect grey lighten-3 light-green-text rounded-element center-align" id="remove_instruction_step"><i class="fas fa-minus-square"></i></a></div></div>'; 

// Add Ingredient to Recipe
$("#add_ingredient").click(function() {
    $("#ingredient-field").append(ingredientField);
    M.updateTextFields();
});
// Remove the Ingredient from Recipe
$("body").on("click","#remove_ingredient", function() {
    $(this).parents(".new-ingredient").remove();
});

// Add Step to Recipe Instructions
$("#add_instruction_step").click(function() {
    $("#steps").append(stepField);
    M.updateTextFields();
});

// Remove the Step from Recipe Instructions
$("body").on("click","#remove_instruction_step", function() {
   $(this).parents(".new-instruction-step").remove();
});
