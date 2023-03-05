

import { Paper } from '@mui/material';
import {  Line } from 'react-chartjs-2';
<<<<<<< Updated upstream


export default function LineVis(){
    
    const labels = ["Jan", "Feb", "Mar", "apr", "may", "jun", "jul"];
=======
import { inferLineGraphLabels, inferLineGraphValues } from './Utils';


function getFormattedData(data){
  
}

export default function LineVis(props){

    // const labels = ["Jan", "Feb", "Mar", "apr", "may", "jun", "jul"];
    // const [labels, setLabels] = React.useState('');
    const labels = inferLineGraphLabels(props.raw_data)
    // console.log(labels)
    const output = inferLineGraphValues(props.raw_data)
    console.log(labels, output)
>>>>>>> Stashed changes
    let data = {
      labels: labels,
      datasets: [{
        label: 'My First Dataset',
        data: [65, 59, 80, 81, 56, 55, 40, 90],
        backgroundColor: 'yellow',
        borderWidth: 1
      },
      {
        label: 'My First Dataset',
        data: [65, 59, 80, 81, 56, 55, 40].reverse(),
        backgroundColor: "red",
        borderWidth: 1
      }]

    };
    
    const config = {
        type: 'line',
        data: data,
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Chart.js Line Chart'
            }
          }
        },
      };
    
    return (
        <Paper variant="outlined" sx={{ height:"350px",alignItems: 'center', width:"700px", marginTop: "10px",
       p:"10px"}} >
        <Line data={data} options={config} />
        </Paper>
    )
}


