import pebl
import json


def mapper(i):
    path = f"data_{i}.in"
    res = {}
    with pebl.syscall.open(path, "rt") as f:
        for line in f:
            for word in line.split():
                if word in res:
                    res[word] += 1
                else:
                    res[word] = 1

    payload = json.dumps(res).encode("ascii")

    conn = pebl.syscall.recv()
    conn.sendall(payload)
    conn.close()


def main():
    i = 0
    mappers = []
    while i < 3:
        if handle:= pebl.syscall.spawn():
            # combiner / controller
            mappers.append(handle)
        else:
            # mapper
            mapper(i)
            import os
            os._exit(0)
        i += 1

    results = {}
    for handle in mappers:
        conn = pebl.syscall.send(handle)
        res = conn.recv(4096).decode("ascii")
        conn.close()
        res = json.loads(res)
        for k, v in res.items():
            if k in results:
                results[k] += v
            else:
                results[k] = v

    return results


def setup():
    text_0 = """
Private cloud
Private cloud is cloud infrastructure operated solely for a single organization, whether managed internally or by a third party, and hosted either internally or externally.[65] Undertaking a private cloud project requires significant engagement to virtualize the business environment, and requires the organization to reevaluate decisions about existing resources. It can improve business, but every step in the project raises security issues that must be addressed to prevent serious vulnerabilities. Self-run data centers[87] are generally capital intensive. They have a significant physical footprint, requiring allocations of space, hardware, and environmental controls. These assets have to be refreshed periodically, resulting in additional capital expenditures. They have attracted criticism because users "still have to buy, build, and manage them" and thus do not benefit from less hands-on management,[88] essentially "[lacking] the economic model that makes cloud computing such an intriguing concept".[89][90]
"""

    with pebl.syscall.open("data_0.in", "wt") as f:
        f.write(text_0)

    text_1 = """
Public cloud
For a comparison of cloud-computing software and providers, see Cloud-computing comparison
Cloud services are considered "public" when they are delivered over the public Internet, and they may be offered as a paid subscription, or free of charge.[91] Architecturally, there are few differences between public- and private-cloud services, but security concerns increase substantially when services (applications, storage, and other resources) are shared by multiple customers. Most public-cloud providers offer direct-connection services that allow customers to securely link their legacy data centers to their cloud-resident applications.[49][92]

Several factors like the functionality of the solutions, cost, integrational and organizational aspects as well as safety & security are influencing the decision of enterprises and organizations to choose a public cloud or on-premises solution.[93]
"""

    with pebl.syscall.open("data_1.in", "wt") as f:
        f.write(text_1)

    text_2 = """
Hybrid cloud
Hybrid cloud is a composition of a public cloud and a private environment, such as a private cloud or on-premises resources,[94][95] that remain distinct entities but are bound together, offering the benefits of multiple deployment models. Hybrid cloud can also mean the ability to connect collocation, managed and/or dedicated services with cloud resources.[65] Gartner defines a hybrid cloud service as a cloud computing service that is composed of some combination of private, public and community cloud services, from different service providers.[96] A hybrid cloud service crosses isolation and provider boundaries so that it can't be simply put in one category of private, public, or community cloud service. It allows one to extend either the capacity or the capability of a cloud service, by aggregation, integration or customization with another cloud service.

Varied use cases for hybrid cloud composition exist. For example, an organization may store sensitive client data in house on a private cloud application, but interconnect that application to a business intelligence application provided on a public cloud as a software service.[97] This example of hybrid cloud extends the capabilities of the enterprise to deliver a specific business service through the addition of externally available public cloud services. Hybrid cloud adoption depends on a number of factors such as data security and compliance requirements, level of control needed over data, and the applications an organization uses.[98]

Another example of hybrid cloud is one where IT organizations use public cloud computing resources to meet temporary capacity needs that can not be met by the private cloud.[99] This capability enables hybrid clouds to employ cloud bursting for scaling across clouds.[65] Cloud bursting is an application deployment model in which an application runs in a private cloud or data center and "bursts" to a public cloud when the demand for computing capacity increases. A primary advantage of cloud bursting and a hybrid cloud model is that an organization pays for extra compute resources only when they are needed.[100] Cloud bursting enables data centers to create an in-house IT infrastructure that supports average workloads, and use cloud resources from public or private clouds, during spikes in processing demands.[101] The specialized model of hybrid cloud, which is built atop heterogeneous hardware, is called "Cross-platform Hybrid Cloud". A cross-platform hybrid cloud is usually powered by different CPU architectures, for example, x86-64 and ARM, underneath. Users can transparently deploy and scale applications without knowledge of the cloud's hardware diversity.[102] This kind of cloud emerges from the rise of ARM-based system-on-chip for server-class computing.

Hybrid cloud infrastructure essentially serves to eliminate limitations inherent to the multi-access relay characteristics of private cloud networking. The advantages include enhanced runtime flexibility and adaptive memory processing unique to virtualized interface models.[103]
"""

    with pebl.syscall.open("data_2.in", "wt") as f:
        f.write(text_2)


setup()
wc = main()
print("word count result:")
for k, v in wc.items():
    print(f"{k}: {v}")
