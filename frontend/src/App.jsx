import { Table } from "antd";
import axios from 'axios';
import { useEffect, useState } from "react";
import { columns } from './components/table/Table.jsx';

function App() {
  const [TableEmployeeData, setTableEmployeeData] = useState()

  const fetchDataTable = () => {
    axios.get('http://127.0.0.1:8000/api/employees/').then(r =>{
      setTableEmployeeData(r.data)
    })
  }

  useEffect( () => {
    fetchDataTable()
  },[])

  return (
    <>
      <div className="header">Сводная таблица сотрудников</div>
      <Table dataSource={TableEmployeeData} columns={columns} pagination={false} rowKey="id"/>
    </>
  )
}

export default App
