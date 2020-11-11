	$(document).ready( function () {
		$('#example').DataTable({
		"ordering": true,
		"info":     true,
		"autoWifth":true,
        columnDefs: [ {
			targets: [ 1 ],
			render: $.fn.dataTable.render.ellipsis(60,false,true)
		} ]
		} );
	} );