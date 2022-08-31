(function() {
    document.getElementById("document")
        .addEventListener("change", handleFileSelect, false);
        
    function handleFileSelect(event) {
        readFileInputEventAsArrayBuffer(event, function(arrayBuffer) {
            mammoth.convertToHtml({arrayBuffer: arrayBuffer})
                .then(displayResult)
                .done();
        });
    }
    
    function displayResult(result) {
//        document.getElementById("messages").value = result.value;
//        $('#messages').text=result.value;
//        $('.cke_wysiwyg_frame').find('body').html(result.value);
//        console.log($('.cke_wysiwyg_frame'))
        
//        var messageHtml = result.messages.map(function(message) {
//            return '<li class="' + message.type + '">' + escapeHtml(message.message) + "</li>";
//        }).join("");
CKEDITOR.instances['messages'].setData(result.value)
//
//        document.getElementById("messages").text = "<ul>" + messageHtml + "</ul>";

    }
    
    function readFileInputEventAsArrayBuffer(event, callback) {
        var file = event.target.files[0];

        var reader = new FileReader();
        
        reader.onload = function(loadEvent) {
            var arrayBuffer = loadEvent.target.result;
            callback(arrayBuffer);
        };
        
        reader.readAsArrayBuffer(file);
    }

    function escapeHtml(value) {
        console.log(value);
        return value
            .replace(/&/g, '&amp;')
            .replace(/"/g, '&quot;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    }
})();
