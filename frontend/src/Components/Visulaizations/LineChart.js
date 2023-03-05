

import { Paper } from '@mui/material';
import React, { useState } from 'react';
import {  Line } from 'react-chartjs-2';

import { inferLineGraphLabels, inferLineGraphValues } from './Utils';


function getFormattedData(data){
  
}

export default function LineVis(props){
  const [datasetIdKey, setdatasetIdKey] = useState();

    // const labels = ["Jan", "Feb", "Mar", "apr", "may", "jun", "jul"];
    // const [labels, setLabels] = React.useState('');
    const labels = inferLineGraphLabels(props.raw_data)
    // console.log(labels)
    const output = inferLineGraphValues(props.raw_data)
    console.log(labels, output)
    let data = {
      labels: labels,
      datasets: output
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
        <Line datasetIdKey={datasetIdKey} data={data} options={config} />
        </Paper>
    )
}
