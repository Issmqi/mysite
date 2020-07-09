#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @date: 2020-07-06 
# @name: testoms
# @author：shimengqi

param=  {
    "billnum": "ec_tradeorder",
    "action": "refundimport",
    "externalData": "[{\"refund_num\":0,\"shopCode\":\"001\",\"refund_id\":\"20190715142010002\",\"tid\":\"292021743163352606\",\"oid\":\"292021743166352606\",\"refund_phase\":\"aftersale\",\"status\":\"SUCCESS\",\"refund_type\":\"1\",\"total_fee\":72.23000000,\"refund_fee\":72.23000000,\"payment\":0,\"buyer_nick\":\"syqhgq\",\"seller_nick\":\"ssaaa\",\"reason\":\"包装/商品破损\",\"desc\":\"\",\"created\":\"2019-07-14 00:00:00\",\"modified\":\"2019-07-14 00:00:00\",\"down_time\":\"2019-07-14 00:00:00\",\"order_status\":\"trade_finished\",\"good_status\":\"BUYER_RECEIVED\",\"sys_status\":\"refund_success\",\"refund_version\":0,\"stored_card_disrefund\":0,\"stored_card_refund\":0,\"refundSourceDetail\":[{\"refund_num\":0,\"stored_card_disrefund\":0,\"stored_card_refund\":0,\"good_status\":\"BUYER_RECEIVED\",\"tid\":\"292021743163352606\",\"oid\":\"292021743166352606\",\"num_iid\":\"577531216623\",\"title\":\"新鲜深海甜虾仁\",\"outer_id\":\"124100460000\",\"num\":1.00000000,\"price\":99.00000000,\"total_fee\":72.23000000,\"payment\":72.23000000,\"refund_fee\":72.23000000,\"created\":\"2019-07-14 00:00:00\",\"modified\":\"2019-07-14 00:00:00\"}]}]"
}
print(sorted(param))

signStr="action=refundimport&billnum=ec_tradeorder&externalData=[{\"refund_num\":0,\"shopCode\":\"001\",\"refund_id\":\"20190715142010002\",\"tid\":\""+tid+"\",\"oid\":\"292021743166352606\",\"refund_phase\":\"aftersale\",\"status\":\"SUCCESS\",\"refund_type\":\"1\",\"total_fee\":72.23000000,\"refund_fee\":72.23000000,\"payment\":0,\"buyer_nick\":\"syqhgq\",\"seller_nick\":\"ssaaa\",\"reason\":\"包装/商品破损\",\"desc\":\"\",\"created\":\"2019-07-14 00:00:00\",\"modified\":\"2019-07-14 00:00:00\",\"down_time\":\"2019-07-14 00:00:00\",\"order_status\":\"trade_finished\",\"good_status\":\"BUYER_RECEIVED\",\"sys_status\":\"refund_success\",\"refund_version\":0,\"stored_card_disrefund\":0,\"stored_card_refund\":0,\"refundSourceDetail\":[{\"refund_num\":0,\"stored_card_disrefund\":0,\"stored_card_refund\":0,\"good_status\":\"BUYER_RECEIVED\",\"tid\":\""+tid+"\",\"oid\":\"292021743166352606\",\"num_iid\":\"577531216623\",\"title\":\"新鲜深海甜虾仁\",\"outer_id\":\"124100460000\",\"num\":1.00000000,\"price\":99.00000000,\"total_fee\":72.23000000,\"payment\":72.23000000,\"refund_fee\":72.23000000,\"created\":\"2019-07-14 00:00:00\",\"modified\":\"2019-07-14 00:00:00\"}]}]"