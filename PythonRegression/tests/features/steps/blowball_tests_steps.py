from aloe import world, step 
from util.test_logic import api_test_logic
from iota import *

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tests = api_test_logic

config = {}
responses = {}
test_vars = {}


@step(r'the returned GTTA transactions will be compared with the milestones')
def compare_gtta_with_milestones(step):
    logger.info("Compare")
    gtta_responses = tests.fetch_response('getTransactionsToApprove')
    find_transactions_responses = tests.fetch_response('findTransactions')
    milestones = list(find_transactions_responses['hashes'])
    node = tests.fetch_config('nodeId')
    config['max'] = len(gtta_responses[node])
    
    transactions = []
    transactions_count = []
    test_vars['milestone_count'] = 0
    
    for node in gtta_responses:
        if type(gtta_responses[node]) is list:
            for response in range(len(gtta_responses[node])):
                branch_transaction = gtta_responses[node][response]['branchTransaction']
                trunk_transaction = gtta_responses[node][response]['trunkTransaction']
                
                compare_responses(branch_transaction,milestones,transactions,transactions_count)
                compare_responses(trunk_transaction,milestones,transactions,transactions_count)
    
        logger.info("Milestone count: " + str(test_vars['milestone_count']))
    
    for transaction in range(len(transactions)):
        logger.debug('Transaction: ' + str(transactions[transaction]) + " : " + str(transactions_count[transaction]))
 
    

@step(r'less than (\d+) percent of the returned transactions should reference milestones')
def less_than_max_percent(step,max_percent):
    percentage = test_vars['milestone_count']/config['max'] * 100.00
    assert percentage < 5
    logger.info(str(percentage) + "% milestones")
    
        
def compare_responses(value,milestone_list,transaction_list,transaction_counter_list):
    if value in milestone_list:
        test_vars['milestone_count'] += 1
        logger.debug('"{}" is a milestone'.format(value))    
    else: 
        if value in transaction_list:
            transaction_counter_list[transaction_list.index(value)] += 1    
        else: 
            transaction_list.append(value) 
            transaction_counter_list.append(1)
            logger.debug('added transaction "{}" to transaction list'.format(value))                                
        
    