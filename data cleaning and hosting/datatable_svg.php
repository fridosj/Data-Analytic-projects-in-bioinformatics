<!DOCTYPE html>
<html>
    <head>
        <title>Varient Details</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
 <style>     
       
      
 <link rel="stylesheet" href=" https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/css/bootstrap.css"/>
      <link rel="stylesheet" href="https://cdn.datatables.net/1.10.23/css/dataTables.bootstrap4.min.css"/>   
div.container {
        width: 80%;
    }
#svgMain {margin-left:auto; margin-right:auto; display:block;}
.bar {
  fill: #aaa;
  height: 21px;
  transition: fill .3s ease;
  cursor: pointer;
  font-family: Helvetica, sans-serif;
}
.bar:hover,
.bar:focus {
  fill: red !important;
  
  text {
    fill: red;
  }
}

body {
  font-family: 'Open Sans', sans-serif;
}

.graph .labels.x-labels {
  text-anchor: middle;
}

.graph .labels.y-labels {
  text-anchor: end;
}


.graph {
  height: 500px;
  width: 800px;
}

.graph .grid {
  stroke: #ccc;
  stroke-dasharray: 0;
  stroke-width: 1;
}

.labels {
  font-size: 13px;
}

.label-title {
  font-weight: bold;
  text-transform: uppercase;
  font-size: 12px;
  fill: black;
}

.data {
  fill: red;
  stroke-width: 1; 
}
figcaption {
  background-color: black;
  color: white;
  font-style: italic;
  padding: 2px;
  text-align: center;
}

</style>
  <link rel="stylesheet" href=" https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.5.2/css/bootstrap.css"/>
      <link rel="stylesheet" href="https://cdn.datatables.net/1.10.23/css/dataTables.bootstrap4.min.css"/>

        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
       
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
        <script src="https://cdn.datatables.net/1.10.23/js/jquery.dataTables.min.js"></script>
        <script src="https://cdn.datatables.net/1.10.23/js/dataTables.bootstrap4.min.js"></script>
      



    </head>
    <body `style="font-family='Calibri';">
        <div>
            <table  id="chr"  class="table table-striped table-bordered" style="width:100%" >
                <thead id='tblhead'>
                <tr>
	<th>RSID</th>
	<th>CHROMOSOMES</th>
        <th>GENE</th>
          <th>GENE_INFO</th>
          <th>TRANS</th>
          <th>REF</th>
          <th>ALT</th>
          <th>REFSEQ</th>
          <th>ALTSEQ</th>
          <th>REFSCORE</th>
          <th>ALTSCORE</th>
          <th>TYPE</th>
	  <th>SCORE</th>  
                </tr>
                </thead>
                <tfoot>
                <tr>
	<th>CHROMOSOMES</th>
        <th>GENE</th>
          <th>GENE_INFO</th>
          <th>TRANS</th>
          <th>RSID</th>
          <th>REF</th>
          <th>ALT</th>
          <th>REFSEQ</th>
          <th>ALTSEQ</th>
          <th>REFSCORE</th>
          <th>ALTSCORE</th>
          <th>TYPE</th>
	  <th>SCORE</th>  
                </tr>
                </tfoot>

                <?php
                    $data=file_get_contents("CHROMOSOMES.json");
                    $data=json_decode($data, true);
                    for($i = 0; $i < sizeof($data["data"]); $i++)
                    {
                        echo '<tr><td>'. $data["data"][$i]["RSID"] .'</td>
                        <td>'. $data["data"][$i]["CHROMOSOMES"] .'</td>
                        <td>'. $data["data"][$i]["GENE"] .'</td>
                        <td>'. $data["data"][$i]["GENE_INFO"] .'</td>
                        <td>'. $data["data"][$i]["TRANS"] .'</td>
                        <td>'. $data["data"][$i]["REF"] .'</td>
                        <td>'. $data["data"][$i]["ALT"] .'</td>
                        <td>'. $data["data"][$i]["REFSEQ"] .'</td>
                        <td>'. $data["data"][$i]["ALTSEQ"] .'</td>      
                        <td>'. $data["data"][$i]["REFSCORE"] .'</td>
                        <td>'. $data["data"][$i]["ALTSCORE"] .'</td>
                        <td>'. $data["data"][$i]["TYPE"] .'</td>
                        <td>'. $data["data"][$i]["SCORE"] .'</td>
                        </tr>';
                        
                    }

                ?>
                
            </table>
    
        </div>
<figure>
  <figcaption>Top mutated genes</figcaption>
<svg width="500" height="500" align="center" id="svgMain"  version="1.2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="graph" aria-labelledby="title" role="img">

<g class="grid x-grid" id="xGrid">
  <line x1="90" x2="90" y1="5" y2="371"></line>
</g>
<g class="grid y-grid" id="yGrid">
  <line x1="90" x2="750" y1="370" y2="370"></line>
</g>

  <g class="labels x-labels">
  <text x="128.5" y="400">9</text>
  <text x="205.5" y="400">10</text>
  <text x="282.5" y="400">11</text>
  <text x="359.5" y="400">12</text>
  <text x="436.5" y="400">13</text>
  <text x="513.5" y="400">14</text>
  <text x="590.5" y="400">15</text>
  <text x="667.5" y="400">16</text>
  <text x="744.5" y="400">17</text>
  <text x="400" y="440" class="label-title">Score Difference</text>
</g>
<g class="labels y-labels">
  <text x="90" y="15">rs148408306</text>
  <text x="90" y="50.8">rs143538724</text> 
  <text x="90" y="86.6">rs191466386</text>
  <text x="90" y="122.4">rs146008053</text>
  <text x="90" y="158.2">rs149521249</text>
  <text x="90" y="194">rs140053393</text>
  <text x="90" y="229.8">rs189758072</text> 
  <text x="90" y="265.6">rs183973249</text>
  <text x="90" y="301.4">rs149080191</text>
  <text x="90" y="337.2">rs186367980</text>
  <text  transform="translate(10,50) rotate(270)" class="label-title">Reference Single Nucleotide Polymorphism</text>
</g>
  <g title="2" class="bar">
    <rect x="90" y="3" width="630.625" height="25" style="fill:red;stroke-width:5;opacity:1"><title>16.624880000000005</title></rect>
  <g title="3" class="bar">
  <g title="2" class="bar">
    <rect x="90" y="35.8" width="617.624" height="25" style="fill:blue;stroke-width:5;opacity:1"><title>16.624040000000008</title></rect>
  <g title="3" class="bar">
    <rect x="90" y="71.6" width="617.623" height="25" style="fill:yellow;stroke-width:5;opacity:1"><title>16.62388999999999</title></rect>
    
  <g title="4" class="bar">
    <rect x="90" y="107.4" width="617.623" height="25" style="fill:purple;stroke-width:5;opacity:1"><title>16.62325</title></rect>
  <g title="5" class="bar">
    <rect x="90" y="143.2" width="615.622" height="25" style="fill:brown;stroke-width:5;opacity:1"><title>16.622880000000002</title></rect>
   
  <g title="6" class="bar">
    <rect x="90" y="179" width="614.622" height="25" style="fill:orange;stroke-width:5;opacity:1"><title>16.622879999999995</title></rect>
   
  <g title="7" class="bar">
    <rect x="90" y="214.8" width="613.622" height="25" style="fill:green;stroke-width:5;opacity:1"><title>16.622789999999995</title></rect>
 
  <g title="8" class="bar">
    <rect x="90" y="250.6" width="612.622" height="25" style="fill:black;stroke-width:5;opacity:1"><title>6.622709999999998</title></rect>

  <g title="9" class="bar">
    <rect x="90" y="286.4" width="611.6226" height="25" style="fill:blue;stroke-width:5;opacity:0.71"><title>16.622640000000004</title></rect>
  
  <g title="10" class="bar">
    <rect x="90" y="322.2" width="611.6224" height="25" style="fill:purple;stroke-width:5;opacity:0.5">><title>16.622420000000005</title></rect>
   

  </g>
</svg>
</figure>
    </body>
</html>
<script>
    $(document).ready(function(){
       
            $('#chr').DataTable({
    columnDefs: [
      { className: "hover", targets: "_all" }, 

    ]
});
             
                });
</script>
