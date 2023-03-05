import * as React from 'react';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import { TypeAnimation } from 'react-type-animation';



export default function Variants(props) {
const text = `Graph Query:\nSome of our debates seem eternal, `
  return (

    <Paper variant="outlined" sx={{display: 'flex', alignItems: 'center', maxWidth: "80%", flexGrow: 0, marginTop: "10px", fontSize: "18px",
      fontFamily: 'system-ui', paddingLeft:"10px", overflowY:"scroll"}} >
      <TypeAnimation
            cursor={false}
            sequence={[
                props.text
            ]}
            speed={80}
            wrapper="pre"
            repeat={1}
      />
    </Paper>
  );
}
