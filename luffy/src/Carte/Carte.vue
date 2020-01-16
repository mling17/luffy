<template>
	<div class="shopping-cart-wrap">
		<h3 class="shopping-cart-tit">我的购物车<small>共1门课程</small></h3>
		<div class="row">
			<el-table
    ref="multipleTable"
    :data="tableData"
    tooltip-effect="dark"
    style="width: 100%"
    @selection-change="handleSelectionChange">
    <el-table-column
      type="selection"
      width="55">
    </el-table-column>
    <el-table-column
      label="日期"
      width="120">
      <template slot-scope="scope">{{ scope.row.date }}</template>
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="120">
    </el-table-column>
    <el-table-column
      prop="address"
      label="地址"
      show-overflow-tooltip>
    </el-table-column>
  </el-table>
		</div>
		<div class="total">
			<el-button type="primary">去结算</el-button>
			<h3>总计: ¥399</h3>	
		</div>
	</div>
</template>

<script>
export default {

};
</script>

<style lang="css" scoped>
.shopping-cart-wrap{
	width: 100%;
}
.shopping-cart-wrap h3,.row{
	width: 1200px;
	margin: 0 auto;
}
.shopping-cart-wrap h3{
	padding: 50px 0 ;
}
.el-table .warning-row {
	background: #22C8C5;
}
.cell img{
	vertical-align: middle;
	width: 170px;
}
.cell a{
	color: #000;
	margin-left: 30px;
}
select {
    border: 0;
    outline: none;
    font-size: 12px;
    color: #666;
    line-height: 18px;
    width: 117px;
    height: 28px;
    padding-left: 16px;
    border: 1px solid #d9d9d9;
    border-radius: 4px;
}
.total{
	width: 1200px;
	margin: 0 auto;
	/*display: flex;*/
	/*justify-content:flex-end;*/

}
.shopping-cart-wrap .total button{
	float: right;
	margin-top: 20px;
}

.shopping-cart-wrap .total h3{
	padding: 0;
	float: right;
	width: 100px;
	height: 30px;
	margin-top: 30px;
}

</style>
