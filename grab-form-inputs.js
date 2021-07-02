//place in footer of document
  (function() {
      //Grab the correct form simply replace form id with hsID of target form
      var form = document.querySelector('form[data-form-id="c6c7797b-7c91-4c47-bbc7-8a6d5cee2b0a"]');
      var values = [];
      var displayFormInputs = function(targetID) {
         //Grabs all of the groups of label/inputs
         var inputGroups = form.querySelectorAll('.hs-form-field');
         for( let i = 0; i < inputGroups.length; i++) {
            //Target InputGroups
            var group = inputGroups[i];
            var input = group.querySelector('input');
            //Ignore submit button
            if (input) {
               //data from target input
               var data = {
                  "label": group.querySelector('label').textContent.replace('*',''),
                  "name": input.name,
                  "value": input.value,
                  }
               // append data to values array
                  values.push(data);
             }        
         };
         for( let i = 0; i < values.length; i++) {
            // Do stuff with the form data
            // This is likely where you want to create some elements 
            // Paste form data into it 
            // And then inject that into the correct place on the DOM.
         }
         //This can be removed. But it will show you if its all working.
         console.log(values);
      }
      //Listens for the submit of the target form
      form.addEventListener('submit', function(e) {
         //Prevents the actual submission
         e.preventDefault();
         // Captures and displays inputs
         displayFormInputs();
         //submits form
         return true;
      });
   })();
