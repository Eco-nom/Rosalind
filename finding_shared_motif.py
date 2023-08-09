# Idea : Sliding Window method (Long to short)
# Load file
f=open('rosalind_lcsm.txt','r')
lst_seq=[]
seq=''
for i in f.readlines():
    if i.startswith('>'):
        lst_seq.append(seq)
        seq=''
    else:
        seq+=i.strip()
lst_seq.append(seq)
lst_seq=lst_seq[1:]

# Function
def finding_shared_motif(motif,lst_seq):
    max_cnt=len(lst_seq)
    cnt=0
    for seq in lst_seq:
        if motif in seq:
            cnt+=1
        else:
            return -1
    if cnt==max_cnt:
        return motif
# 
lst_motif=[] # Shared motif list
for window_size in list(range(0,len(lst_seq[0])+1))[::-1]:
    start=0
    while True:
        end=start+window_size
        if end==len(lst_seq[0]):
            motif=lst_seq[0][start:end]
            if finding_shared_motif(motif,lst_seq)!=-1:
                print(motif)
                break
            break
        else:
            motif=lst_seq[0][start:end]
            start+=1
            if finding_shared_motif(motif,lst_seq)!=-1:
                lst_motif.append(motif)
                break

print(lst_motif[0]) # Longest shared motif
