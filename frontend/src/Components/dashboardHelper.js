// import logo from './logo.svg';

import React from 'react';
import { connect } from 'react-redux';
import { recommendVisualization } from './Visulaizations/Utils';

function DashboardHelper(props) {
const {data} = props;
const [useLinegraph, setUseLinegraph] = React.useState(Boolean);
//   const saveDashboard = async ()=>{

//     try{
//       set_sending_request("true")
//       const res = await axios.post(`${backend_url}/api/v1/dashboard/${data?.id}`, {
//       wallet_address: wallet_address,
//     })
//     // enqueueSnackbar('Saved Dashboard');
//     set_sending_request(false)
//   }
//     catch{
//       set_sending_request(false)
//       enqueueSnackbar('Server error!!');
//     }
//   }

if (data && data.output && data?.output.length >1 && recommendVisualization(data?.output) === 'line-chart'){
    props.setPredictedVis("line-chart")
    setUseLinegraph(true);
   }

  return (
    <>
     
    </>
  )
}
const mapStateToProps = state => {
  return {
    wallet_address: state.counter.wallet_address,
  }
}
export default connect(mapStateToProps)(DashboardHelper);
