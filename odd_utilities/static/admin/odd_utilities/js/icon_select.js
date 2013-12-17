(function($){
	var IconSelect = {};
	
	IconSelect.setRelatedImage = function(selectElement) {
		var displayElement = selectElement.siblings(".icon-select-image-display");
		displayElement.empty();
		
		var output = [];
		
		// Place icon for each selected value; supports multiple select
		selectElement.find(":selected").each(function() {
			var image = $(this).data("related-image");

            if (typeof image !== "undefined")
			    output.push('<img src="' + image + '" alt="">')
		});
		
		displayElement.html(output.join("\n"));
	}
	
    $(function(){
    
		$(".icon-select").each(function() {
			IconSelect.setRelatedImage($(this));
		
			$(this).change(function() {
				IconSelect.setRelatedImage($(this));
			});
		});
    });
}(django.jQuery));