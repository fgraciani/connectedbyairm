	$(document).ready( function () {
		$('#example').DataTable({
		"ordering": true,
		"info":     true,
		"autoWifth":true,
    "order": [[ 1, "asc" ]]
		} );
	} );