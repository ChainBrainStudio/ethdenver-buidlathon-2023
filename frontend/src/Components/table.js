import * as React from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import { connect } from 'react-redux';
import { CircularProgress } from '@mui/material';
import {humanize as h} from "@jsdevtools/humanize-anything"
import humanize from 'humanize-plus';
import Variants, { TypeWriter } from './Visulaizations/textarea';
import RowRadioButtonsGroup from './input/Radio';
import BarVis from './Visulaizations/BarGraph';
import LineVis from './Visulaizations/LineChart';
import PieVis from './Visulaizations/Pie';
import BubbleVis from './Visulaizations/Bubble';
import Footer from './footer';
import Feedback from './input/feedback';
import Table_ from './Visulaizations/table_';


export function buildColumns(data){
    let column_header = Object.keys(data[0]);
    var columns = []

    for (var index = 0; index < column_header.length; index++)
    {
        columns.push({id: column_header[index], label: column_header[index], minWidth: 170, align: "center",format: (value) => {
          if(typeof(value) == "number"){
            return humanize.formatNumber(value, 2)
          }
          else{

          return h(value)} }})

    }

    return columns

}

export function StickyHeadTable(props) {
  let columns, rows, data_present;

  let {data, visualization} = props;
 const data_ = data?.output
  if(data_ && Object.keys(data_).length !== 0){
    data_present = true;
  }
  else{
    data_present = false;
  }
//   console.log(props.data);

  if(data_ && data_present){
        columns = buildColumns(data_);
        rows = data_
  }
  else{
    columns = []
    rows=[]
  }
  if(props.isLoading){
    return (
      <CircularProgress sx={{ align: 'center', marginTop:"10px",} }  color="secondary"/>
  )}
  else{
     // const tree = `Alive = True; \n while Alive:
//   try:
 //    hard();
  //   except Exception as in life:
  //    jumpOverIt();
  //    tryagain();`


  return (
    
            <>
            {/* <TypeWriter content={tree} speed={100}/> */}
          {data?.chatgpt_gql && <Variants text={`GraphQL Query:\n ${data.chatgpt_gql}`}/>}
          {data_present &&  
          <RowRadioButtonsGroup/>}
          {data_present && visualization == "table" && <Table_ rows={rows} columns={columns}/>
  }



      {data_present && visualization == "bar-graph" && (<BarVis/>)}


      {data_present && visualization == "line-chart" && (<LineVis raw_data={data_}/>)}


      {data_present && visualization === "pie-chart" && (<PieVis/>)}


      {data_present && visualization === "bubble" && (<BubbleVis/>)}

    {data_present &&
      <Footer/>
    }
    {data_present &&
      <Feedback/>
    }
    </>
  );
}}

const mapStateToProps = state => {
    return {
      data: state.counter.data,
      isLoading: state.counter.isLoading,
      visualization: state.counter.visualization
    }
  }

export default connect(mapStateToProps)(StickyHeadTable)
