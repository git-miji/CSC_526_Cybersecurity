#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <linux/inet.h>

/* This is the structure we shall use to register our function */
static struct nf_hook_ops Net_Filter_Hook;

/* This is the hook function itself */
unsigned int Net_Filter(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)

{
	struct iphdr *iph;
	struct tcphdr *tcph;
	iph = ip_hdr(skb);
	tcph = (void *)iph+iph->ihl*4;

/* Dropping outbound Telnet Traffic */

	if (iph->protocol == IPPROTO_TCP && tcph->dest == htons(23) && iph->saddr == in_aton("10.0.2.6") && iph->daddr == in_aton("10.0.2.7"))
	{
		printk(KERN_INFO "Drpping packet from %d.%d.%d.%d to %d.%d.%d.%d",
		((unsigned char *)&iph->saddr) [0],
		((unsigned char *)&iph->saddr) [1],
		((unsigned char *)&iph->saddr) [2],
		((unsigned char *)&iph->saddr) [3],
		((unsigned char *)&iph->daddr) [0],
		((unsigned char *)&iph->daddr) [1],
		((unsigned char *)&iph->daddr) [2],
		((unsigned char *)&iph->daddr) [3]);
		
		return NF_DROP;
	}
	
	else
	
	{
		return NF_ACCEPT;
	}

}
/* Initialization routine */
int setupFilter(void)
	{ /* Fill in our hook structure */
	Net_Filter_Hook.hook = Net_Filter; /* Handler function */
	Net_Filter_Hook.hooknum = NF_INET_POST_ROUTING; /* First hook for IPv4 */
	Net_Filter_Hook.pf = PF_INET;
	Net_Filter_Hook.priority = NF_IP_PRI_FIRST; /* Make our function first */
	nf_register_net_hook(&init_net, &Net_Filter_Hook);
	return 0;
	}

/* Cleanup routine */

void removeFilter(void)
{	printk(KERN_INFO "Filter is being removed\n");
	nf_unregister_net_hook(&init_net, &Net_Filter_Hook);
}
module_init(setupFilter);
module_exit(removeFilter);

MODULE_LICENSE("GPL");
