	$(document).ready( function () {
		$('#example').DataTable({
		"ordering": true,
		"info":     true,
		"autoWifth":true,
        columnDefs: [ {
			targets: [ 2 ],
			render: $.fn.dataTable.render.ellipsis(40,false,true)
		} ]
		} );
	} );