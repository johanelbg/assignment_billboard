$('#form').hide()

$('.plusButton').on('click', function(){
    $('#displayForm').hide()
    $('#form').show()
})

$('.cancelButton').on('click', function(){
    $('#displayForm').show()
    $('#form').hide()
})
