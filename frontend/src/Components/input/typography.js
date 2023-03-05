import * as React from 'react';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import { TypeAnimation } from 'react-type-animation';



export default function Typography_(props) {
const text = `Graph Query:\nSome of our debates seem eternal, `
  return (

    <Paper variant="outlined"  sx={{backgroundColor: 'transparent',display: 'flex', alignItems: 'center', maxWidth: "80%", flexGrow: 0, marginTop: "10px", fontSize: "36px",
      fontFamily: 'system-ui',fontWeight: 'bold', paddingLeft:"10px", overflowY:"scroll", paddingTop:"10px", paddingBottom:"10px", color:"white"}} >
      {props.text}
    </Paper>
  );
}
