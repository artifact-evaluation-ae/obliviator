# OBLIVIATOR: OBLIVIous Parallel Joins and other OperATORs in Shared Memory Environments


This is the artifact repository of Obliviator [9]. Our work is in full accordance with the USENIX'25 ethics guidelines. We propose new algorithms and implement systems with a positive impact on preserving data privacy. Our experiments involved neither testing on live systems without prior consent, nor human participants.

All our tests were executed either on synthetic datasets whose creation we describe or on already publicly available real-world datasets. They include TPC-H, a synthesized benchmark with created contents, a twitter social graph that is available to the public and contains the anonymized topology of the Twitter social network (also used in [1, 2, 3]), a public IMDb dataset that contains the public information of title names and actors (used in [4, 5]), a public Amazon dataset that records frequently co-purchased products (used in [5, 6]), a joke dataset that contains anonymous ratings of jokes by different users (used in [5, 7]), and slashdot dataset that contains technology news website with friend/foe links between users (used in [5, 8]). We would like to point out that none of these benchmarks/datasets can cause any type of harm and are strictly used to evaluate our algorithms.

Additionally, we open-source all artifacts required for recreating our algorithms and experiments. They include all our code in this paper, scripts to generate the synthesized dataset, scripts to process public benchmarks and datasets, configuration information, and scripts to reproduce our evaluation.

Please refer to **./artifact_availability.pdf** for artifact evaluation phase-1, artifact availability.

Please refer to **./artifact_appendix.pdf** for artifact evaluation phase-2, artifact functionality.

**Please feel free to pull issues or reach out to us for any troubleshooting.**

&nbsp;


&nbsp;

References


[1] Meeyoung Cha, Hamed Haddadi, Fabricio Benevenuto, and Krishna P. Gummadi. Measuring User Influence in Twitter: The Million Follower Fallacy. In In Proceedings of the 4th International AAAI Conference on Weblogs and Social Media (ICWSM).

[2] Zhao Chang, Dong Xie, Sheng Wang, and Feifei Li. Towards practical oblivious join. In Proceedings of the 2022 International Conference on Management of Data. Association for Computing Machinery, 2022.

[3] Xiang Li, Nuozhou Sun, Yunqian Luo, and Mingyu Gao. Soda: A set of fast oblivious algorithms in distributed secure data analytics. Proceedings of the VLDB Endowment, 16(7):1671–1684, 2023.

[4] Kevin Lewi and David J Wu. Order-revealing encryption: New constructions, applications, and lower bounds. In Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security, pages 1167–1178, 2016.

[5] Shuyuan Li, Yuxiang Zeng, Yuxiang Wang, Yiman Zhong, Zimu Zhou, and Yongxin Tong. An experimental study on federated equi-joins. IEEE Transactions on Knowledge and Data Engineering, 2024.

[6] Jaewon Yang and Jure Leskovec. Defining and evaluating network communities based on ground-truth. In Proceedings of the ACM SIGKDD Workshop on Mining Data Semantics, pages 1–8, 2012.

[7] Ken Goldberg, Theresa Roeder, Dhruv Gupta, and Chris Perkins. Eigentaste: A constant time collaborative filtering algorithm. information retrieval, 4:133–151, 2001.

[8] Jure Leskovec, Daniel Huttenlocher, and Jon Kleinberg. Signed networks in social media. In Proceedings of the SIGCHI conference on human factors in computing systems, pages 1361–1370, 2010.

[9] Apostolos Mavrogiannakis, Xian Wang, Ioannis Demertzis, Dimitrios Papadopoulos, and Minos Garofalakis. OBLIVIATOR: Oblivious parallel joins and other operators in shared memory environments. Cryptology ePrint Archive, Paper 2025/183, 2025.