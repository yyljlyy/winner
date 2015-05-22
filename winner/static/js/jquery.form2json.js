
(function($){	
	function paramString2obj (serializedParams) {    
	    var obj={};
	    function evalThem (str) {
			var attributeName = str.split("=")[0];
			var attributeValue = str.split("=")[1];
			if(!attributeValue){
			    return ;
			}
			eval(attributeName+"='"+attributeValue+"',");
			var array = attributeName.split(".");
			for (var i = 1; i < array.length; i++) {
			    var tmpArray = Array();
			    tmpArray.push("obj");
			    for (var j = 0; j < i; j++) {
					tmpArray.push(array[j]);
			    };
			    var evalString = tmpArray.join(".");
			    if(!eval(evalString)){
					eval(evalString+"={};");               
			    }
			};
			eval("obj."+attributeName+"='"+attributeValue+"';");
	    };
	    var properties = serializedParams.split("&");
	    for (var i = 0; i < properties.length; i++) {
	    	evalThem(properties[i]);
	    };
	    return obj;
	};
	 
	$.fn.form2json = function(){
		 var o = {};
	    var a = this.serializeArray();
	    $.each(a, function() {
	        if (o[this.name]) {
	            if (!o[this.name].push) {
	                o[this.name] = [ o[this.name] ];
	            }
	            o[this.name].push($.trim(this.value) || '');
	        } else {
	            o[this.name] = $.trim(this.value) || '';
	        }
	    });
	    return o;
	};
})(jQuery);