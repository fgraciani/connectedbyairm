	$(document).ready( function () {
		$('#example').DataTable({
		"ordering": true,
		"info":     true,
		"autoWifth":true,
        columnDefs: [ {
			targets: [ 3 ],
			render: $.fn.dataTable.render.ellipsis(15,false,true)
		} ]
		} );
	} );