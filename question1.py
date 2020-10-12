#Identifying the uniques emails


class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unq_emails={}
        unq_emails_total=0
        for email in emails:
            split_email = email.split("@",1)
            local,domain = split_email[0], split_email[1]
            local_split=local.split("+")
            local_without_plus=local_split[0]
            local_joined=local_without_plus.replace('.', '')
            if (local_joined,domain) not in unq_emails:
                unq_emails[(local_joined,domain)]="exists"
                unq_emails_total+=1
                
        return unq_emails_total