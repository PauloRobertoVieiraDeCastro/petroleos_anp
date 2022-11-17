
/*function mudar(){
	var radios = document.getElementById("codigo").value;
	if(radios=='tipo'){
		console.log('tipo')
		let div = document.getElementById('grafico2');
  		div.classList.toggle('hide');
	}else{
		console.log('caract')
	}
}*/

$(document).ready(function(){
    $("select").change(function(){
    	$(this).find("option:selected").each(function(){
    		var v = $(this).attr("value");
    		if(v=='caracte'){
    			$("#grafico1").hide(1000);
    			$("#grafico2").show(1000);
    		}else{
    			$("#grafico2").hide(1000);
    			$("#grafico1").show(1000);
    		}
    	})
    })
})
