// import logo from './logo.svg';

import { CircularProgress } from '@mui/material';
import React from 'react';
import { connect } from 'react-redux';
import Typography_ from './input/typography';
import { buildColumns } from './table';
import LineVis from './Visulaizations/LineChart';
import Table_ from './Visulaizations/table_';
import Variants from './Visulaizations/textarea';
import { recommendVisualization } from './Visulaizations/Utils';


function DashboardHelper(props) {
    const {data, user_input, chatgpt_gql} = props;
    const columns = buildColumns(data);
    const rows = data
    const [useLinegraph, setUseLinegraph] = React.useState(Boolean);

if (data && data.output && data?.output.length >1 && recommendVisualization(data?.output) === 'line-chart'){
    setUseLinegraph(true);
   }

  return (
    <>
        <Typography_  text={`${user_input}`}/>
        <Variants text={`GraphQL Query:\n ${chatgpt_gql}`}/>
        <Table_ rows={rows} columns={columns} />
        {useLinegraph && (<LineVis raw_data={data}/>)}
        <br/><br/>
    </>
  )
}
const mapStateToProps = state => {
  return {
    wallet_address: state.counter.wallet_address,
  }
}
export default connect(mapStateToProps)(DashboardHelper);
