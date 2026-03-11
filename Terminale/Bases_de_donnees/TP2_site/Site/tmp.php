<script>
			function logout() {
				<?php $authOk = false; ?>
			}
		</script>


<?php 
	if($authOK == false) {
		header ('location: index.php');
	}
 ?>