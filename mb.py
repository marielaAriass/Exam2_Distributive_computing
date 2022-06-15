{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "01ecac92",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Incorrect format. Upload failed\n"
     ]
    }
   ],
   "source": [
    "import subprocess,sys,re\n",
    "\n",
    "MB=\"A\"*(1024*1024)\n",
    "\n",
    "def mb(ip,MBs,verbose=False):\n",
    "    with open('tmp','w') as t:\n",
    "        for i in range(0,int(MBs)):\n",
    "            t.write(MB)\n",
    "        t.close()\n",
    "    r=subprocess.run(f\"time scp tmp {ip}\", shell=True, check=True,capture_output=True)\n",
    "    out=r.stderr.decode(\"ASCII\")\n",
    "    time_s=re.match(\".*system.([\\d:\\.]+)\",out.strip()).group(1)\n",
    "    tlist=time_s.replace(\".\",\":\").split(\":\")\n",
    "    time=int(tlist[0])*60+int(tlist[1])+int(tlist[2])*.01\n",
    "    try:\n",
    "        subprocess.run(f\"rm {ip}\",shell=True,check=True)\n",
    "    except:\n",
    "        pass\n",
    "    subprocess.run(f\"rm tmp\",shell=True,check=True)\n",
    "    if(verbose):\n",
    "        print(time, \"s\") \n",
    "    return time\n",
    "    \n",
    "if(__name__==\"__main__\"):\n",
    "    if(len(sys.argv)!=3):\n",
    "        print(\"Usage: mb.py IP MB_size\")\n",
    "    else:\n",
    "        try:\n",
    "            mb(sys.argv[1],sys.argv[2],verbose=True)\n",
    "        except:\n",
    "            print(\"Incorrect format. Upload failed\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "701be282",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
