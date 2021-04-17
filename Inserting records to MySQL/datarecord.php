<!DOCTYPE html>
<html>
<body>
<?php
    $connection = mysqli_connect("127.0.0.1","root","","patient_data");

    $sql = "select * from patient_info";
    $result = mysqli_query($connection, $sql);

    //create an array
    $emparray = array();
    while($row =mysqli_fetch_assoc($result))
    {
        $emparray[] = $row;
    }
     json_encode($emparray);

    //close the db connection
    mysqli_close($connection);
?>
<?php
    $fp = fopen('parsed.json', 'w');
    fwrite($fp, json_encode($emparray));
    fclose($fp);
?>
<?php

$json=file_get_contents("parsed.json");
$myObject = json_decode($json);
?>
<input type="text" id="myInput" onkeyup="myFunction()" placeholder="Search..">

<table id="myTable" border='1'>

<tr>
	<td>Diagnosis_Age</td>
	<td>Sex</td>
	<td>Ethnicity_Category</td>
	<td>Histology</td>
	<td>Adjuvant_Treatment</td>
        <td>ECOG_Performance_Status</td>
 	<td>Smoking_History</td>
	<td>Person_Cigarette_Smoking_History_Pack_Year_Value</td>
	<td>Relapse_Free_status</td>
	<td>Relapse_Free_status_months</td>
	<td>Ubiquitous_Assay_Panel</td>
	<td>Percent_Necrosis</td>
	<td>Tumor_Volume_cm3</td>
	<td>Tumor_Stage</td>
	<td>Positron_emission_tomography_tumor_background_ratio</td>
	<td>cfDNA_Input_ng</td>
	<td>Lymph_Node_Involvement</td>
	<td>Ki67_Percentage</td>
	<td>CT_Slice_Spacing</td>
	<td>patient_id</td>
</tr>
<?PHP
foreach($myObject as $key=>$item)
{
	?>
	<tr>
		<td><?PHP echo $item->Diagnosis_Age; ?></td>
		<td><?PHP echo $item->Sex; ?></td>
		<td><?PHP echo $item->Ethnicity_Category; ?></td>
		<td><?PHP echo $item->Histology; ?></td>
		<td><?PHP echo $item->Adjuvant_Treatment; ?></td>
		<td><?PHP echo $item->ECOG_Performance_Status; ?></td>
		<td><?PHP echo $item->Smoking_History; ?></td>
		<td><?PHP echo $item->Person_Cigarette_Smoking_History_Pack_Year_Value; ?></td>
		<td><?PHP echo $item->Relapse_Free_Status; ?></td>
		<td><?PHP echo $item->Relapse_Free_Status_Months; ?></td>
		<td><?PHP echo $item->Ubiquitous_Assay_Panel; ?></td>
		<td><?PHP echo $item->Percent_Necrosis; ?></td>
		<td><?PHP echo $item->Tumor_Volume_cm3; ?></td>
		<td><?PHP echo $item->Tumor_Stage; ?></td>
		<td><?PHP echo $item->Positron_emission_tomography_tumor_background_ratio; ?></td>
		<td><?PHP echo $item->cfDNA_Input_ng; ?></td>
		<td><?PHP echo $item->Lymph_Node_Involvement; ?></td>
		<td><?PHP echo $item->Ki67_Percentage; ?></td>
		<td><?PHP echo $item->CT_Slice_Spacing; ?></td>
		<td><?PHP echo $item->patient_id; ?></td>
	</tr>
	<?PHP

}
?>
</table>
<script>
function myFunction() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}
</script>
</body>
</html>
